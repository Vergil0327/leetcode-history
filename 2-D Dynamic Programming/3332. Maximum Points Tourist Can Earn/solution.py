class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [[0]*n for _ in range(k+1)]

        for i in range(k):
            for cur in range(n):
                for nxt in range(n):
                    if nxt == cur:
                        dp[i+1][cur] = max(dp[i+1][cur], dp[i][cur] + stayScore[i][cur])
                    else:
                        dp[i+1][nxt] = max(dp[i+1][nxt], dp[i][cur] + travelScore[cur][nxt])
        return max(dp[k])