class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[0]*5 for _ in range(n+1)] # 0: "a", 1: "e", 2: "i", 3: "o", 4: "u"
        vowel2idx = {ch: i for i, ch in enumerate("aeiou")}
        
        for i in range(5):
            dp[0][i] = 1
        
        for i in range(n):
            dp[i+1][vowel2idx["a"]] += dp[i][vowel2idx["e"]]
            dp[i+1][vowel2idx["e"]] += dp[i][vowel2idx["a"]] + dp[i][vowel2idx["i"]]
            dp[i+1][vowel2idx["i"]] += dp[i][vowel2idx["a"]] + dp[i][vowel2idx["e"]] + dp[i][vowel2idx["o"]] + dp[i][vowel2idx["u"]]
            dp[i+1][vowel2idx["o"]] += dp[i][vowel2idx["i"]] + dp[i][vowel2idx["u"]]
            dp[i+1][vowel2idx["u"]] += dp[i][vowel2idx["a"]]

            dp[i+1][vowel2idx["a"]] %= mod
            dp[i+1][vowel2idx["e"]] %= mod
            dp[i+1][vowel2idx["i"]] %= mod
            dp[i+1][vowel2idx["o"]] %= mod
            dp[i+1][vowel2idx["u"]] %= mod

        return sum(dp[n-1]) % mod
