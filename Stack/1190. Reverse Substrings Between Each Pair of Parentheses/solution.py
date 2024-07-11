class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = [""]
        i = 0
        while i < n:
            if s[i] == "(":
                j = i+1
                while j < n and s[j].isalpha():
                    j += 1
                
                stack.append(s[i+1:j])
                i = j-1
            elif s[i] == ")":
                rev = stack.pop()[::-1]
                stack[-1] += rev
            else:
                j = i
                while j < n and s[j].isalpha():
                    j += 1
                stack[-1] += s[i:j]
                i = j-1
            i += 1

        return stack[-1]
