class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        curr = 0
        res = 0
        signs = [1]
        sign = 1
        
        n = len(s)
        for i in range(n):
            ch = s[i]
            if ch == " ": continue
            
            if ch.isnumeric():
                curr = int(ch) + curr * 10
            else:
                match ch:
                    case "+":
                        res += curr * sign
                        sign = 1
                        curr = 0
                    case "-":
                        res += curr * sign
                        sign = -1
                        curr = 0
                    case "(":
                        stack.append(res)
                        signs.append(sign)
                        sign = 1
                        res = 0
                    case ")":
                        res += curr * sign
                        res *= signs.pop()
                        res += stack.pop()
                        curr = 0

        return res + curr * sign

class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        signs = [1]
        sign = 1
        
        n = len(s)
        i = 0
        while i < n:
            ch = s[i]

            if ch.isnumeric():
                curr = 0
                while i<n and s[i].isnumeric():
                    curr = curr * 10 + int(s[i])
                    i += 1
                
                res += curr * sign
            else:
                match ch:
                    case " ":
                        i += 1
                    case "+":
                        sign = signs[-1]
                        i += 1
                    case "-":
                        sign = signs[-1] * -1
                        i += 1
                    case "(":
                        signs.append(sign)
                        i += 1
                    case ")":
                        signs.pop()
                        i += 1
        return res