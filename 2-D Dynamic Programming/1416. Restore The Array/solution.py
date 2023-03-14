class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = int(1e9+7)
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1

        s = "$" + s
        MAX_DIGIT = len(str(k))
        for i in range(1, n+1):
            num = base = 0
            for j in range(i, 0, -1):
                substr = s[j:i+1]
                if len(substr) > MAX_DIGIT: break

                # num = int(substr)
                num = num + int(s[j]) * 10**base
                base += 1
                if num > k: break
                if len(substr) > 1 and substr[0] == '0': continue # leading zeros
                if 1 <= num <= k:
                    dp[i] += dp[j-1]
                    dp[i] %= MOD
        return dp[n]%MOD

class Solution_TLE:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = int(1e9+7)
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1

        s = "$" + s
        for i in range(1, n+1):
            for j in range(i, 0, -1):
                substr = s[j:i+1]
                num = int(substr)
                if num > k: break
                if len(substr) > 1 and substr[0] == '0': continue # leading zeros
                if 1 <= num <= k:
                    dp[i] += dp[j-1]
                    dp[i] %= MOD
        return dp[n]%MOD