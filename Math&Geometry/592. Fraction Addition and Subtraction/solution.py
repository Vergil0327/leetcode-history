class Solution:
    def fractionAddition(self, expression: str) -> str:
        if expression[0] != "-":
            expression = "+" + expression

        n = len(expression)

        nums = []
        ops = []
        i = 0
        for j in range(n):
            if expression[j] in {"-", "+"}:
                ops.append(expression[j])
                nums.append(expression[i:j])
                i = j+1
        nums.append(expression[i:])
        
        numerators = []
        denominators = []
        for num in nums:
            if not num: continue

            numerator, denominator = num.split("/")
            numerators.append(int(numerator))
            denominators.append(int(denominator))

        GCD = gcd(*denominators)
        denominator = GCD
        for num in denominators:
            denominator *= num//GCD
        
        numerator = 0
        for i in range(len(ops)):
            cur = numerators[i] * (denominator//denominators[i])
            
            if ops[i] == "+":
                numerator += cur
            else:
                numerator -= cur

        GCD = gcd(numerator,denominator)
        return f"{numerator//GCD}/{denominator//GCD}"
    

# Concise Version
class Solution:
    def fractionAddition(self, expression: str) -> str:
        arr = expression.replace("+", " +").replace("-", " -").split()
        
        numerator, denominator = 0, 1
        for num in arr:
            a, b = num.split("/")
            a, b = int(a), int(b)
            numerator = (numerator*b) + (denominator*a)
            denominator *= b

            divisor = math.gcd(numerator, denominator)
            numerator //= divisor
            denominator //= divisor

        return f"{numerator}/{denominator}"