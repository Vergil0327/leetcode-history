class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        totState = 1<<n
        dp = [inf] * totState
        dp[0] = 0
        for state in range(totState):
            time = 0
            for i in range(n):
                if (state>>i)&1:
                    time += tasks[i]
            if time <= sessionTime:
                dp[state] = 1

        for state in range(totState):
            subset = state
            while subset:
                dp[state] = min(dp[state], dp[subset] + dp[state-subset])
                subset = (subset-1)&state

        return dp[totState-1]