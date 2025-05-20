# Intuition

k個subarray, 每個subarray.size至少m

1 <= nums.length <= 2000
1 <= k <= floor(nums.length / m)
1 <= m <= 3

直覺想到能用top-down DP:

```py
class Solution:
    def maxSum(self, nums: List[int], K: int, m: int) -> int:
        n = len(nums)

        @cache
        def dfs(i, k):
            if k == 0: return 0
            if i >= n: return -inf
            
            res = dfs(i+1, k)
            
            subarray_sum = 0
            for j in range(i, n):
                subarray_sum += nums[j]
                if j-i+1 >=m:
                    res = max(res, dfs(j+1, k-1) + subarray_sum)
            return res
        
        return dfs(0, K)
```

time: O(n*k*n) => TLE

後來在優化了一下, 加上限制確保能湊出K個至少m size的subarray, 但仍TLE

```py
class Solution:
    def maxSum(self, nums: List[int], K: int, m: int) -> int:
        n = len(nums)

        presum = list(accumulate(nums, initial=0))
        @cache
        def dfs(i, k):
            if k == 0: return 0
            if i >= n: return -inf
            
            res = -inf
            if k*m <= n-i:
                res = dfs(i+1, k)
            for j in range(i+m-1, n-(k-1)*m):
                res = max(res, dfs(j+1, k-1) + presum[j+1]-presum[i])
            return res
        
        return dfs(0, K)
```

代表我們必須拉掉`for j in range(i+m-1, n-(k-1)*m)`這項, 讓時間複雜度降到O(nk)

由於subarray大小至少要`m`, 所以我們狀態轉移可以直接`dfs(i+m, k-1) + sum(nums[i] for i in range(i, i+m))`

而`sum(nums[i] for i in range(i, i+m))`這項我們能用prefix sum來優化
但題意是說至少大小為`m`, 我們也能繼續往後延伸, 所以我們額外加個狀態來表示我們是否能繼續往後在同個subarray加入nums[i], 所以我們定義

`def dfs(i, k, appending): the maximum sum of k non-overlapping subarrays of nums[:i], where each subarray has a length of at least m and we can still append nums[i] to current subarray based on `appending` state`

那麼我們就有三種狀態轉移:

```py
# skip
res = dfs(i+1, k, False)

# keep appending
if appending:
    res = max(res, dfs(i+1, k, appending) + nums[i])

# get 1 valid subarray
if k>0 and i+m <= n:
    res = max(res, dfs(i+m, k-1, True) + presum[i+m]-presum[i])
```

base case:

```py
# considering all nums. it's valid only if k==0 which means we get k subarrays at least
if i >= n: return 0 if k == 0 else -inf

if n-i < k*m: return -inf # can't get k subarrays at least from remain nums[i:]
```