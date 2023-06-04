class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10**9+7

        while len(num1) < len(num2):
            num1 = "0"+num1

        n = len(num2)
        memo = [[[[-1]*(max_sum+1) for _ in range(2)] for _ in range(2)] for _ in range(n)]
        def calculate(i, isLowerbound, isUpperbound, total):
            if total < 0: return 0
            if i == n: return 1

            lo = int(num1[i]) if isLowerbound else 0
            hi = int(num2[i]) if isUpperbound else 9
            
            if memo[i][isLowerbound][isUpperbound][total] != -1:
                return memo[i][isLowerbound][isUpperbound][total]

            res = 0
            for c in range(lo, hi+1):
                res += calculate(
                    i+1,
                    1 if isLowerbound and c == lo else 0,
                    1 if isUpperbound and c == hi else 0,
                    total-c)
                res %= mod
            
            memo[i][isLowerbound][isUpperbound][total] = res
            return res
            
        total = calculate(0, 1, 1, max_sum)
        invalid = calculate(0, 1, 1, min_sum-1)
        return ((total-invalid)%mod + mod)%mod
