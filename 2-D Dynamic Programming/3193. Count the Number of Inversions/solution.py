class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7

        requirements.sort()

        mxCnt = max(r[1] for r in requirements)

        dp = [[0] * (mxCnt + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for length in range(1, n + 1):
            for inversions in range(mxCnt + 1):
                if dp[length - 1][inversions] == 0:
                    continue

                for pos in range(length):
                    if inversions + pos <= mxCnt:
                        dp[length][inversions + pos] = (
                            dp[length][inversions + pos] + dp[length - 1][inversions]
                        ) % MOD

            for endi, cnti in requirements:
                if endi + 1 == length:
                    for inv in range(mxCnt + 1):
                        if inv != cnti:
                            dp[length][inv] = 0

        return sum(dp[n]) % MOD
