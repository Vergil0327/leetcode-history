class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seqSet = set(nums)
        
        length = 0
        for num in seqSet:
            if num-1 not in seqSet:
                i = num
                while i+1 in seqSet:
                    i += 1
                length = max(length , i-num+1 )
        return length