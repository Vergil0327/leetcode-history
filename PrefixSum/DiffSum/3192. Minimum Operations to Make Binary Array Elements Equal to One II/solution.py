# see leetcode 995. Minimum Number of K Consecutive Bit Flips
# since we must flip if (nums[i]+flips[i]) % 2 == 0, use difference array to store accumulated flips
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        flips = [0]*(n+1)
        res = 0
        for i in range(n):
            flips[i] += flips[i-1]
            
            if (nums[i]+flips[i])%2==0:
                flips[i] += 1
                flips[-1] -= 1
                res += 1
        
        return res
        