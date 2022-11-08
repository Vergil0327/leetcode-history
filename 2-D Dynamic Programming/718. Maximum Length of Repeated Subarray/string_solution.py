# since the answer is actually longest length of common prefix
# we can turn into string problem
# ord(num) is only valid for num is within [0.. 65535]
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        str1 = "".join([chr(num) for num in nums1])
        str2 = ""
        
        maxLen = 0
        for ch in map(chr, nums2):
            str2 += ch
            if str2 in str1: # found common prefix
                maxLen = max(maxLen, len(str2))
            else:
                str2 = str2[1:] # keep exploring common prefix
        return maxLen
