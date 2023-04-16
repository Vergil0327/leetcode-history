class Solution:
    def addMinimum(self, word: str) -> int:
        res = 0
        stack = []
        for ch in word:
            if ch == "a":
                if stack and stack[-1] == "b": # missing c before
                    res += 1
                if stack and stack[-1] == "a": # missing b c before
                    res += 2

            if ch == "b":                
                if not stack: # missing a before
                    res += 1
                else:                        
                    if stack[-1] == "b": # missing c a before
                        res += 2
                    if stack[-1] == "c": # missing a before
                        res += 1

            if ch == "c":
                if not stack:
                    res += 2 # ab
                else:
                    if stack[-1] == "a":
                        res += 1 # b
                        
                    if stack[-1] == "c":
                        res += 2 # ab
            stack.append(ch)

        # missing after
        if stack[-1] != "c":
            if stack[-1] == "a":
                res += 2
            if stack[-1] == "b":
                res += 1
        return res
    

# Wise Solution
# keep track of missing character of "abc"
class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        res, missing = 0, 3
        for i in range(n):
            if i > 0 and word[i-1] >= word[i]:
                res += missing
                missing = 3
            missing -= 1
        return res + missing