class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        mod = 1000000007

        n = len(vals)
        child = [[] for _ in range(n)]
        for u in range(1, n):
            child[par[u]].append(u)

        # if vals[node] has duplicate digit, it's invald
        valid = set()
        for node, val in enumerate(vals):
            s = str(val)
            if len(s) == len(set(s)): # no duplicate digits
                valid.add(node)
                    

        def dfs(node):
            dp = {0: 0}
            s = str(vals[node])
            if node in valid:
                state = sum(1 << int(c) for c in s)
                dp[state] = vals[node]

            for nxt in child[node]:
                dp_nxt = dfs(nxt)
                for state_nxt, val_nxt in dp_nxt.items():
                    for state, val in list(dp.items()):
                        if state & state_nxt == 0:
                            dp[state | state_nxt] = max(dp.get(state | state_nxt, 0), val + val_nxt)

            self.res += max(dp.values())
            return dp

        self.res = 0
        dfs(0)
        return self.res % mod