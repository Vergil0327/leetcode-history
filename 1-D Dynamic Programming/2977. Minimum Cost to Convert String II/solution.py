class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        m = len(original)

        dist = defaultdict(lambda: defaultdict(lambda: inf))
        for s, t, c in zip(original, changed, cost):
            dist[s][s] = 0
            dist[s][t] = min(dist[s][t], c)

        for mid in set(original+changed):
            for src in set(original):
                for dst in set(changed):
                    dist[src][dst] = min(dist[src][dst], dist[src][mid] + dist[mid][dst])
        
        dp = [inf] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for s in dist:
                if i >= len(s) and source[i-len(s):i] in dist and target[i-len(s):i] in dist[source[i-len(s):i]]:
                    dp[i] = min(dp[i], dp[i-len(s)] + dist[source[i-len(s):i]][target[i-len(s):i]])

            if source[i-1] == target[i-1]:
                dp[i] = min(dp[i], dp[i-1])

        return dp[n] if dp[n] < inf else -1
