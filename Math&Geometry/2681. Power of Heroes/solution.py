class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        nums.sort()
        nums = [0] + nums
        
        res = 0
        presum = 0
        for i in range(1, n+1):
            res += nums[i]**2 * nums[i] % mod

            # total = 0
            # for j in range(i):
            #     total += nums[j] * (2**(i-j-1))
            
            res = (res + nums[i]**2 * presum % mod) % mod
            presum = presum*2 + nums[i]
        return res


class Solution_TLE:
    def sumOfPower(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        nums.sort()
            
        res = 0
        for i in range(n):
            total = nums[i]**2 * nums[i]
            for j in range(i-1, -1, -1):
                total += nums[i]**2 * nums[j] * (2**(i-j-1)) % mod

            res = (res + total)%mod

        return res
        