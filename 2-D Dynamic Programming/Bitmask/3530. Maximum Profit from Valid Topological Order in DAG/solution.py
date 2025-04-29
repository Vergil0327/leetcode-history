class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        parent = [0] * n
        for u, v in edges:
            parent[v] |= (1<<u)

        total_states = 1<<n
        dp = [-1]*total_states
        dp[0] = 0

        for state in range(total_states):
            if dp[state] == -1: continue

            pos = state.bit_count() + 1
            for node in range(n):
                if (state>>node)&1: continue # already removed

                if (state&parent[node]) == parent[node]:
                    new_state = state | (1<<node)
                    dp[new_state] = max(dp[new_state], dp[state] + score[node] * pos)

        return dp[total_states-1]