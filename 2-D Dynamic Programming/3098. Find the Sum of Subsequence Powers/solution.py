mod = 1000000007
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        n = len(nums)
        
        @cache
        def dfs(i, prev, size, power):
            if size == 0: return power
            if i == n: return 0
            
            power1 = dfs(i+1, prev, size, power)
            power2 = dfs(i+1, i, size-1, min(power, nums[i]-nums[prev] if prev != -1 else inf))
            
            
            return (power1+power2)%mod
            
        return dfs(0, -1, k, inf)