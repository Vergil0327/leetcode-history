# Intuition

```
Example 2: Input: arr = [2,1,3,4,4]

[2,1,3,4,4]
 0 1 2 3 4   index

[1,2,3,4,4] sorted
 1 0 2 3 4

Input = [2,1,4,4,3]
         0 1 2 3 4
        [1,2,3,4,4] sorted
         1 0 4 2 3        
```

首先能看到, 如果在i位置作為partition, 代表arr[:i]這段就確立位置了
這時如果suffix arr[i+1:]裡有任何一個數他排序後的位置是在sorted_arr[:i]的話, 將不可能將arr透過這個partition變成sorted
那代表這個partition是不合法的

再來能想到的是, 目標要求**the largest number of chunks we can make to sort the array**
數據量**arr.length <= 2000** => 以leetcode標準來看能接受到O(n^2)
所以往dynamic programming這方向來試試看

首先先照著題目要求得去定義dp[i]: the largest number of chunks we can make to sort the array[:i]

```
arr = X X X X X X {X X X X X X X}
                   j           i
```

再來根據一開始的想法去思考每個chunk, 由於不確定chunk在哪, 所以我們都遍歷看看
以dynamic programming來說, 我們就思考當前以arr[i]結尾的chunk

如果我們選擇arr[j:i]作為一個chunk, 並且arr[j:i]這段元素的排序後的index皆大於arr[:i-1]裡的每個元素的排序後位置
代表這段arr[j:i]chunk是可以被獨立拆出來的
此時dp[i] = dp[j-1] + 1
由於j可以往回遍歷, 因此dp[i] = max(dp[i], dp[j-1]+1) if arr[j:i] is valid

在得到這個關係式之後, 就只差如何高效去查看arr[j:i]是不是合法chunk了
框架會像是:

```py
def maxChunksToSorted(self, arr: List[int]) -> int:
    n = len(arr)

    arr = [-1] + arr # to 1-indexed
    for i in range(1, n+1):
        for j in range(i, 0, -1):
            if check(arr[j:i]):
                dp[i] = max(dp[i], dp[j-1]+1)
    return dp[n]
```

最終返回dp[n]: the largest number of chunks we can make to sort the array[:n]

有了這想法後再來要解決的就是helper function `check`

對於一段arr[j:i], 我們要判斷是不是合法chunk, 首先裡面每個元素在排序後的位置都必須大於prefix arr[:j-1]

所以如果我們知道arr[:i]每個元素的排序後位置的話, 只要滿足`max_sorted_index(arr[:j-1]) < min_sorted_index(arr[j:i])`
就能更新`dp[i] = max(dp[i], dp[j-1]+1)`


因此我們可以先建立maxSortedIdxFromLeft[i]代表: max_sorted_index for prefix array `arr[:i]`

```py
n = len(arr)
arr = [-1] + arr # to 1-indexed

# construct maxSortedIdxFromLeft
arr2 = list(sorted([arr[i], i] for i in range(n+1)))
MAP = defaultdict(list)
for i, (_, originalIdx) in enumerate(arr2):
    MAP[originalIdx] = i

maxSortedIdxFromLeft = [0]
for i in range(1, n+1):
    maxSortedIdxFromLeft.append(max(maxSortedIdxFromLeft[-1], MAP[i]))
```

然後:

```py
dp = [0] * (n+1)
for i in range(1, n+1):
    minIdx = inf
    for j in range(i, 0, -1):
        minIdx = min(minIdx, MAP[j])

        if maxSortedIdxFromLeft[j-1] < minIdx:
            dp[i] = max(dp[i], dp[j-1]+1)
return dp[n]
```

time: O(n^2) 
space: O(n)