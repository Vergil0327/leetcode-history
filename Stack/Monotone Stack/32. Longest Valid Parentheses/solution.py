class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                if stack and s[stack[-1]] == "(":
                    # we can't update maxLen here. it can't cover "()()"
                    # maxLen = max(maxLen, i-stack[-1]+1)
                    stack.pop()
                    maxLen = max(maxLen, i - stack[-1] if stack else i+1)
                    # ")()()" -> maxLen: 0 -> 2 -> 4
                    # "()())" -> maxLen: 0 -> 2 -> 4
                else:
                    stack.append(i)
        return maxLen