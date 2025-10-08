class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = [] # ['(', # of '('] or [')', # of ')']
        for ch in s:
            if ch == '(':
                if stack and stack[-1][0] == '(':
                    stack[-1][1] += 1
                else:
                    stack.append(["(", 1])
            else:
                if stack and stack[-1][0] == ')':
                    stack[-1][1] += 1
                else:
                    stack.append([")", 1])
                
                if stack[-1][1] == k:
                    if len(stack) >= 2:
                        if stack[-2][1] >= k:
                            stack.pop()
                            stack[-1][1] -= k
                            if stack[-1][1] == 0:
                                stack.pop()
        
        return "".join([ch for ch, cnt in stack for _ in range(cnt)])