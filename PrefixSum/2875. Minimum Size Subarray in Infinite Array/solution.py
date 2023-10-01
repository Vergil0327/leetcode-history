class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        presum = list(accumulate(nums))
        
        k = 0
        while target > presum[n-1]:
            target -= presum[n-1]
            k += 1
        
        seen = {}
        seen[0] = -1
        res = inf
        for i in range(n):
            if (pre := presum[i]-target) in seen:
                res = min(res, i-seen[pre])
            seen[presum[i]] = i
            
        for i in range(n):
            if (pre := presum[i]+presum[n-1]-target) in seen:
                res = min(res, i+n-seen[pre])
        
        if res == inf: return -1
        return res + k*n

# Concise
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        k = target // total
        target %= total
        if target == 0:
            return k * n

        dp = {0: -1}
        cur = 0
        res = inf
        for i, num in enumerate(nums + nums):
            cur += num
            if cur - target in dp:
                res = min(res, i - dp.get(cur - target))
            dp[cur] = i
        return res + k * n if res < inf else -1