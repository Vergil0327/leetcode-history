class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-","*","/"}:
                stack.append(int(token))
            else:
                if token == "+":
                    top = stack.pop()
                    stack[-1] += top
                if token == "-":
                    top = stack.pop()
                    stack[-1] -= top
                if token == "*":
                    top = stack.pop()
                    stack[-1] *= top
                if token == "/":
                    top = stack.pop()
                    # python strange behavior, be careful of divisiton of negative number
                    # 6 // -10 should be 0, towards to 0. also correct in other language
                    # but in python, 6 // -10 == -1
                    stack[-1] =  int(stack[-1]/top)

        return stack[0]