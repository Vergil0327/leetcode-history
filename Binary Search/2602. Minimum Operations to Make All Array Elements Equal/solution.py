class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]
        
        
        res = []
        for q in queries:
            op = 0
            i = bisect_left(nums, q)
            op += abs(q*i - presum[i])
            op += abs((n-i)*q - (presum[n]-presum[i]))
            
            res.append(op)
        return res