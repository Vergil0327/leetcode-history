class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        t = str(n)
        tLength = len(t)

        res = 0
        for l in range(1, tLength):
            res += len(digits) ** l

        sameDigit = []
        for i in range(tLength):
            j = bisect.bisect_right(digits, t[i])
            if digits[j-1] == t[i]:
                res += (j-1) * len(digits)**(tLength-i-1)
                sameDigit.append(digits[j-1])
            else:
                res += j * len(digits)**(tLength-i-1)
                break
        return res + (1 if len(sameDigit) == tLength else 0)

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        t = str(n)
        tLength = len(t)

        res = 0
        for l in range(1, tLength):
            res += len(digits) ** l

        def dfs(i):
            nonlocal res
            
            if i == tLength:
                res += 1
                return

            for d in digits:
                if d < t[i]:
                    res += pow(len(digits), tLength-1-i)
                elif d == t[i]:
                    dfs(i+1)
        dfs(0)
        return res