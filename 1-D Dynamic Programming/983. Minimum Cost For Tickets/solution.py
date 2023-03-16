class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        dp = [inf] * (n+1)
        dp[0] = 0

        days = [days[0]] + days
        ticketType = [1, 7, 30]
        for i in range(1, n+1):
            for j in range(i, 0, -1):
                if days[i] - days[j]+1 > ticketType[-1]: break
                for k in range(3):
                    if days[i] - days[j]+1 <= ticketType[k]:
                        dp[i] = min(dp[i], dp[j-1] + costs[k])
        return dp[n]