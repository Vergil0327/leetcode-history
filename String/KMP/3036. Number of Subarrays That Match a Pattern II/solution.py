class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        s = ""
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                s += "a"
            elif nums[i+1] < nums[i]:
                s += "b"
            else:
                s += "c"
        
        target = ""
        for num in pattern:
            if num > 0:
                target += "a"
            elif num < 0:
                target += "b"
            else:
                target += "c"
                
        # kmp preprocess
        def preprocess(s):
            n = len(s)
            lps = [0]*n
            lps[0] = 0
            for i in range(1, n):
                j = lps[i-1]
                while j > 0 and s[i] != s[j]:
                    j = lps[j-1]
                lps[i] = j + int(s[i] == s[j])
            return lps
        
        lps = preprocess(target)
        
        n = len(s)
        
        j = res = 0
        for i in range(n):
            while j > 0 and s[i] != target[j]:
                j = lps[j-1]
            j = j + (s[i] == target[j])
            
            if j == len(target):
                j = lps[j-1]
                res += 1

        return res
