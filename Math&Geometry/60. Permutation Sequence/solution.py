class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            num = 1
            for i in range(1, n+1):
                num *= i
            return num

        digits = [i for i in range(1, n+1)] # 1-9
        res = ""
        i = 1 # considering i-th digit
        while i <= n:
            permutation = factorial(n-i) # # this is how many permutations we can get if we fix first i idx
            idx = (k+permutation-1) // permutation - 1 # = ceil(k / permutation)-1
            res += str(digits[idx])
            
            digits.pop(idx)
            k -= idx * permutation
            i+=1
        
        return res
