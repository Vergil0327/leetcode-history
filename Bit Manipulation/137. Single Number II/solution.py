# time: O(32n)
# space: O(32)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                bits[i] += (num>>i)&1
        
        res = 0
        for i in range(32):
            res |= (bits[i]%3)<<i
        
        return res if res < (1<<31) else res - (1<<32)