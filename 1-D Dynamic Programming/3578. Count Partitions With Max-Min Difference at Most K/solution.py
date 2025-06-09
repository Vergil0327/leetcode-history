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