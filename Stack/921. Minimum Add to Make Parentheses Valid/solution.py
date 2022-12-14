class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for c in s:
            if c == "(":
                stack.append(c)
            if c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    res += 1
        return res + len(stack)