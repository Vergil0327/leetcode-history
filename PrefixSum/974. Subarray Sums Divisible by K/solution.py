class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1 # base case
        
        presum = 0
        res = 0
        for num in nums:
            presum += num
            m = presum % k
            res += count[m]
            count[m] += 1
            
        return res
