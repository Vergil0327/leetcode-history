class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        
        operation = "+"
        curr = 0
        stack = []

        def calculate(ch):
            nonlocal operation, curr
            if operation == "+":
                stack.append(curr)
            elif operation == "-":
                stack.append(-curr)
            elif operation == "*":
                stack[-1] *= curr
            elif operation == "/":
                # 需要python 除法向 0 取整
                # python strange behavior: -3 // 2 = -2
                stack[-1] = int(stack[-1] / curr)
            curr = 0
            operation = ch
        
        for i in range(n):
            if s[i] == " ": continue
            
            if s[i].isdigit():
                curr = int(s[i]) + curr * 10
            else:
                calculate(s[i])

        calculate("") # last round
        return sum(stack)