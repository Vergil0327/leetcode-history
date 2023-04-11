class Solution:
    def palindromePartition(self, s: str, K: int) -> int:
        n = len(s)

        dp = [[inf] * (K+1) for _ in range(n+1)] # 1-indexed
        s = "#" + s # to 1-indexed

        # base case
        dp[0][0] = 0
        # dp[0][k] = inf # invalid

        @lru_cache(None)
        def isPal(l, r) -> int:
            swap = 0
            while l < r:
                if s[l] != s[r]:
                    swap += 1
                l, r = l+1, r-1
            return swap

        for i in range(1, n+1):
            for k in range(1, K+1):
                for j in range(i, k-1, -1):
                    swap = isPal(j, i)
                    if swap == 0: # already palindrome
                        dp[i][k] = min(dp[i][k], dp[j-1][k-1])
                    else:
                        dp[i][k] = min(dp[i][k], dp[j-1][k-1] + swap)
        return dp[n][K]


# X X X X X X [X X X]
#              j   i
