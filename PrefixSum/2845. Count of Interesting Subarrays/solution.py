class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        isValid = [0]*n
        for i in range(n):
            if nums[i]%modulo == k:
                isValid[i] = 1
                
        presum = 0
        count = defaultdict(int)
        count[0] = 1
        res = 0
        for i in range(n):
            presum += isValid[i]
            if presum >= modulo:
                presum %= modulo
            res += count[(presum-k+modulo)%modulo]
            
            count[presum] += 1 
        return res