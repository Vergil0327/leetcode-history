# Intuition

### simulate process (TLE)

```py
mod = 1000000007
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def dfs(i):
            if i >= n: return 1

            mn = mx = nums[i]
            res = 0
            for j in range(i, n):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                if mx-mn <= k:
                    res += dfs(j+1)
                    res %= mod
                else:
                    break
            return res
        return dfs(0)
```
    
### method 2

for valid parition, it reminds me of sliding window.
through sliding window, we can find each nums[i]'s farthest valid nums[j] which nums[i:j] is valid partition

if define dp[i]: the total number of ways to partition nums[:r] under this condition.
it'll become:

```py
mod = 1000000007
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)

        sl = SortedList()
        l = r = 0
        dp = [1] + [0] * n
        while r < n:
            sl.add(nums[r])
            r += 1
            while l < r and sl[-1]-sl[0] > k:
                sl.remove(nums[l])
                l += 1

            # All indices from l to r are valid
            # So the segment starting at l can end at r
            for i in range(l, r):
                dp[r] += dp[i]
                dp[r] %= mod
        return dp[n]
```

now, it's quite clear for me to optimize.

we can keep recording the sum of partition through sliding window, keep updating dp[l:r) in variable `ways`

```py
mod = 1000000007
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        dp = [1] + [0] * n
        l = r = ways = 0
        sl = SortedList()
        while r < n:
            ways = (ways + dp[r]) % mod
            sl.add(nums[r])
            r += 1

            while l < r and sl[-1]-sl[0] > k:
                ways = ((ways - dp[l]) + mod) % mod
                sl.remove(nums[l])
                l += 1

            dp[r] = ways
        return dp[n]
```
