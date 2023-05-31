Intuition

use sliding window to find a window whose sum equals target,
and store every valid windows's length and choose minimum of two

since answer must be 2 non-overlapping, we also store start-point and endpoint.

then sort by start-point, and we create a suffix min length `dp` where dp[i] means the minimum length within valid_windows[i:], i.e. min(valid_windows[i:])

```
___
 ___
  ____
     ____
```

then we use two-pointers to find valid answer.
for each valid_windows[i], we move j until the start-time of valid_windows[j] is strictly greater than valid_windows[i]

```py
res = inf
j = 0
for i in range(m):
    while j < m and valids[j][1] <= valids[i][2]:
        j += 1

    if j != m:
        res = min(res, valids[i][0] + suffixMin[j])
    
return res if res != inf else -1
```

# Other Solution - 3 Pass + DP

target = prefix_sum[i] - prefix_sum[j]
所以prefix_sum[j] = prefix_sum[i] - target
我們可以用hashmap來看prefix_sum[j]存不存在, 如果存在代表我們能找出一段和為target的subarray
其中 hashmap紀錄的是`{prsum_j: index}`

然後我們可以用利用prefix sum + hashmap來找出`sum(subarray) == target`的兩個端點
同時我們在利用兩端點來計算出subarray的長度
我們再利用一個predp來紀錄截至`arr[:i]`為止的總和為target的最短長度

同樣的, 我們也能用suffix sum + hashmap來找出`sum(subarray) == target`的兩個端點
然後一樣用sufdp來紀錄截至`arr[i:]`為止總和為target的最短長度

然後在遍歷每個位置一遍, 利用predp[i]+sufdp[i]找出以`i`為分界, 兩邊的最短合法subarray長度相加

這邊要注意的是hashmap的base case
hashmap `sumIdx`紀錄的是{sum: index}
- 所以prefix sum時, `sumIdx = {0: 0}`
  - 代表和為0時index=0, 因為prefix sum是1-indexed, 這樣當i=1, arr[i-1]=target時, 我們才能透過sumIdx[presum[i]-target]-i求出length.
- 同理, suffix sum時 `sumIdx = {0: n}`. (遍歷suffix sum時是0-indexed)

```py
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        presum = [0] * (n+1)
        sumIdx = {0: 0}
        predp = [inf] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + arr[i-1]
            if (t := presum[i]-target) in sumIdx:
                predp[i] = min(i - sumIdx[t], predp[i-1])
            else:
                predp[i] = predp[i-1]
            sumIdx[presum[i]] = i

        sufsum = [0] * (n+1)
        sumIdx = {0: n}
        sufdp = [inf] * (n+1)
        for i in range(n-1, -1, -1):
            sufsum[i] = sufsum[i+1] + arr[i]
            if (t := sufsum[i]-target) in sumIdx:
                sufdp[i] = min(sufdp[i+1], sumIdx[t]-i)
            else:
                sufdp[i] = sufdp[i+1]
            sumIdx[sufsum[i]] = i

        res = inf
        for i in range(n):
            res = min(res, predp[i]+sufdp[i])

        return res if res != inf else -1
```