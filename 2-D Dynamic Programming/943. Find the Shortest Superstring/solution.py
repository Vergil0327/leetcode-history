class Solution:
    def findDistance(self, i, j, A):
        s, t = A[i], A[j]
        m, n = len(s), len(t)
        for k in range(min(m, n), -1, -1):
            if s[m-k:] == t[:k]:
                return n-k
        return 0

    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        max_state = 1<<n

        dp = [[inf]*n for _ in range(max_state)]
        parent = [[-1]*n for _ in range(max_state)]
        
        dist = [[-1]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if j != i:
                    dist[i][j] = self.findDistance(i, j, words)

        # base case
        for i in range(n):
            dp[1<<i][i] = len(words[i])

        for state in range(max_state):
            for last_pick in range(n):
                if (state>>last_pick)&1 == 0: continue
                prev_state = state - (1<<last_pick)
                if prev_state == 0: continue # can't find prev_last_pick

                for prev_last_pick in range(n):
                    if (prev_state>>prev_last_pick)&1 == 0: continue
                    if (cur := dp[prev_state][prev_last_pick] + dist[prev_last_pick][last_pick]) < dp[state][last_pick]:
                        dp[state][last_pick] = cur
                        parent[state][last_pick] = prev_last_pick

        length = inf
        last_pick = ""
        for last in range(n):
            if dp[max_state-1][last] < length:
                length = dp[max_state-1][last]
                last_pick = last

        state = max_state-1
        path = [last_pick]
        while parent[state][last_pick] != -1:
            prev = parent[state][last_pick]
            path.append(prev)

            state = state - (1<<last_pick)
            last_pick = prev

        res = ""
        def merge(s, t):
            m, n = len(s), len(t)
            for k in range(min(m, n), -1, -1):
                if s[m-k:] == t[:k]:
                    return s+t[k:]
            return s+t

        for idx in reversed(path):
            res = merge(res, words[idx])
        return res
