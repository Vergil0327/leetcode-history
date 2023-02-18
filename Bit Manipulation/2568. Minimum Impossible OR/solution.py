class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:        
        SET = set(nums)
        missing = 1
        while missing < int(1e9):
            if missing not in SET: return missing
            missing <<= 1
        return missing