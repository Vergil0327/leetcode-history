class Solution:
    def minDifficulty(self, jobDifficulty: List[int], D: int) -> int:
        if D > len(jobDifficulty): return -1

        n = len(jobDifficulty)
        dp = [[inf] * (D+1) for _ in range(n+1)]

        # base case
        dp[0][0] = 0

        jobDifficulty = [0] + jobDifficulty # to 1-indexed

        for i in range(1, n+1):
            for d in range(1, min(i, D)+1):
                difficulty = -inf
                for j in range(i, -d, -1):
                    difficulty = max(difficulty, jobDifficulty[j])
                    dp[i][d] = min(dp[i][d], dp[j-1][d-1]+difficulty)
        return dp[n][D]