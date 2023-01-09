class Solution:
    def lengthLongestPath(self, s: str) -> int:
        strs = s.split("\n")
        curr = 0
        maxLen = 0
        stack = []
        def isFile(s):
            return "." in s
        
        for s in strs:
            if not stack:
                countTab = s.count("\t")
                
                stack.append([s[countTab:], countTab])
                curr += len(s[countTab:])
            else:
                countTab = s.count("\t")

                while stack and countTab != stack[-1][1]+1:
                    t, _ = stack.pop()
                    curr -= len(t)+1 # 1 for backslash
                stack.append([s[countTab:], countTab])
                curr += len(s[countTab:])+1 # 1 for backslash
            
            if stack and isFile(stack[-1][0]):
                maxLen = max(maxLen, curr)
        
        return maxLen if stack and isFile(stack[-1][0]) else 0