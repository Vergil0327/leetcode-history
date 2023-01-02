class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        XOR = 0 # num1 ^ num2 where num1, num2 are our target
        for num in nums:
            XOR ^= num
        
        # if XOR = 1101, every 1 position means num1 and num2 differ in this bit
        # find least significant bit to split nums into possible num1 and possible num2
        lsb = XOR & -XOR

        # since num1 ^ num2 differ in this `lsb` bit position
        # let's say:
        # if num & lsb == 1, num might be num1
        # if num & lsb == 0, num. might be num2
        # XOR again and we can remove duplicate and leave num1 & num2
        res = [0, 0]
        for num in nums:
            if num & lsb:
                res[0] ^= num
            else:
                res[1] ^= num
        return res