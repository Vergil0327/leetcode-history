# Math
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        
        # first digit can't be 0. thus, we have 9 options. (1-9)
        # first digit can be 0. therefore, we still have 9 options
        permutationChoices = [9,9,8,7,6,5,4,3,2,1]

        # n=1 -> 1 digits
        # n=2 -> 2 digits
        digits = min(n, 10)
        product = 1
        res = 1 # for `0`. ps. `0` is valid unique digit but leading zeros are not
        for i in range(digits):
            product *= permutationChoices[i]
            res += product
        return res

# backtracking
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 0
        digits = [str(i) for i in range(10)]
        def backtracking(state, n):
            nonlocal res
            if n == 0:
                res += 1
                return

            for d in digits:
                non_leading_zeros_state = str(int(state))

                # unique digits or single digit "0" "1" ... "9"
                if d not in non_leading_zeros_state or non_leading_zeros_state == "0":
                    backtracking(state+d, n-1)
        backtracking("0", n)
        return res