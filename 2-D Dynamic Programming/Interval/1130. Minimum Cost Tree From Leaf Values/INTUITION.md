# Intuition

首先我們觀察最後一步, 他會是

```
tree = arr = [X X X X X X] [X X X X X X X X]
              i         k  k+1            j
                 lmax            rmax
```

整棵樹(arr[i:j])的和 = 左子樹合併Cost + 右子樹合併Cost + left_subtree_max * right_subtree_max

也就是我們可以這麼定義dp:
dp[i][j]: smallest possible sum of the values of each non-leaf node within arr[i:j]

然後根據上面敘述, 狀態轉移為
`dp[i][j] = dp[i][k] + lmax * rmax + dp[k+1][j]`

如此一來我們便能從小區間到大區間, bottom-up的方式一路往上遍歷所有可能(brute force with memorization)來求出最佳解

left_subtree_max 我們可以再找中間`k`的時候由左往就順便找出來
righ_subtree_max 則透過max heap並搭配index來把不在範圍內的給pop掉
```py
dp = [[inf]*n for _ in range(n)]

for length in range(1 ,n+1):
    for i in range(n-length+1): # j = i+length-1 < n
        j = i+length-1

        lmax = -inf
        maxHeap = [(-num, i) for i, num in enumerate(arr[i:j+1])]
        heapq.heapify(maxHeap)

        for k in range(i, j):
            lmax = max(lmax, arr[k])
            
            while maxHeap and maxHeap[0][1] <= k:
                heapq.heappop(maxHeap)
            rmax = -maxHeap[0][0]

            dp[i][j] = min(dp[i][j], dp[i][k] + lmax * rmax + dp[k+1][j])
```

那這邊注意一下邊界條件

當length=1時, 其實沒有意義, 我們會看到我們並不會進到dp表達式更新dp[i][j]
實際上的確也至少要兩個節點才能合併

所以length=1的情況我們單獨處理, 然後從i=2開始

那對於length=1的情況, 也就是子樹為單一節點時, 那麼此時cost就是為0
所以:
```py
# length=1
for i in range(n):
    dp[i][i] = 0
```

那最終答案就是看整個區間的smallest sum: dp[0][n-1]

# Optimized Solution

實際上整個過程就是取兩個數相消, 小的消失、大的留著
因此對於每個arr[i]來說:
- 他要不是因為離他最近的prev_greater_value而消除
- 就是因為被離他最近的next_greater_value給消除
- 而此時的cost = arr[i] * min(prev_greater_value, next_greater_value)

我們可以從最小的數`nums[i]`開始消，此時他肯定是被他左邊或右邊的給消除
我們就這兩個決策取最小的值, greedily消除`nums[i]`
所以整個O(n^2)的過程可以寫成:
```py
res = 0
while len(arr) > 1:
    num = min(arr)
    idx = arr.index(num)
    cost = num * min(arr[idx-1:idx] + arr[idx+1:idx+2]) # 這樣寫有個好處是可以順便handle左邊沒有值或右邊沒有值的情況
    res += cost
return res
```

但根據一開始分析可發現, 我們要找的prevGreater跟nextGreater都可以透過monotonic stack來以O(1)時間得知

所以
```py
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [inf]
        for num in arr:
            while stack[-1] <= num:
                mid = stack.pop()
                res += mid * min(stack[-1], num) # stack[-1]: previous greater value; num: next greater value

            stack.append(num)

        # stil exist some value without next greater element
        while len(stack) > 2:
            mid = stack.pop()
            res += mid * stack[-1] # stack[-1]: previous greater
        return res
```