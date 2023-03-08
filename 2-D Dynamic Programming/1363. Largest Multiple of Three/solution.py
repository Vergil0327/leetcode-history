class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        n = len(digits)
        digits.sort(key = lambda x:-x)
        digits = [0] + digits

        dp = [["inf"]*3 for _ in range(1+n)]
        dp[0][0] = ""

        def better(s1, s2):
            if s2 == "inf": return True
            if len(s1) > len(s2):
                return True
            elif len(s1) < len(s2):
                return False
            else:
                return float(s1)>float(s2)

        for i in range(1, n+1):
            mod = digits[i] % 3
            for j in range(3):
                dp[i][j] = dp[i-1][j] # not choose ditis[i]
                if dp[i-1][(j-mod+3)%3] == "inf": continue

                if better(dp[i-1][(j-mod+3)%3] + str(digits[i]), dp[i-1][j]): # if we choose digits[i] and it's better
                    dp[i][j] = dp[i-1][(j-mod+3)%3] + str(digits[i])
        
        # edge case: remember to remove leading zeros
        # ex. dp[n][0] = "00000"
        i = 0
        while i < len(dp[n][0])-1 and dp[n][0][i] == "0":
            i += 1
        return dp[n][0][i:]
        
# Optimized
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        n = len(digits)
        digits.sort(key = lambda x:-x)
        digits = [0] + digits

        dp = [[-inf]*3 for _ in range(1+n)]
        dp[0][0] = 0
        pick = [[(False, -1)]*3 for _ in range(1+n)]

        for i in range(1, n+1):
            mod = digits[i] % 3
            for j in range(3):
                dp[i][j] = dp[i-1][j] # not choose ditis[i]
                pick[i][j] = (False, j)

                if dp[i-1][(j-mod+3)%3] + 1 > dp[i-1][j]: # if we choose digits[i] and it's better
                    dp[i][j] = dp[i-1][(j-mod+3)%3] + 1
                    pick[i][j] = (True, (j-mod+3)%3)
        
        res = ""
        i, j = n, 0
        while i > 0:
            if pick[i][j][0]:
                res += str(digits[i])
            j = pick[i][j][1]
            i -= 1
        res = res[::-1]

        i = 0
        while i < len(res)-1 and res[i] == "0":
            i += 1
        return res[i:]
