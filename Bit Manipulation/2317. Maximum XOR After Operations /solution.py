class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        # res = 0
        # for num in nums:
        #     for i in range(32):
        #         bit = ((num>>i)&1)
        #         res |= (bit<<i)
        # return res
        res = 0
        for num in nums:
            res |= num
        return res
