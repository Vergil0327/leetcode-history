# Intuition

### brute force

```
class Solution:
    @cache
    def find_max(self, i, state, nums):
        if i >= len(nums): return 0

        mod = 1000000007
        # skip
        res = self.find_max(i+1, state, nums) % mod

        # take
        digit_state = 0
        for c in str(nums[i]):
            digit_state |= (1<<int(c))

        if state&digit_state == 0: # no duplicate digit
            res = max(res, (self.find_max(i+1, state|digit_state, nums) + nums[i]) % mod)
        return res

    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        mod = 1000000007
        child = [[] for _ in range(len(par))]

        for node, p in enumerate(par):
            if p > -1:
                child[p].append(node)

        # if vals[node] has duplicate digit, it's invald
        for node, val in enumerate(vals):
            s = str(val)
            for d in range(10):
                if s.count(str(d)) > 1:
                    vals[node] = 0
                    break

        
        self.res = 0
        def dfs(node):
            subtree = [vals[node]]
            for nxt in child[node]:
                subtree += dfs(nxt)
            subtree = list(filter(lambda x:x > 0, subtree))

            self.res += self.find_max(0, 0, tuple(subtree))
            self.res %= mod
            return subtree
        dfs(0)
        
        return self.res % mod
```

Since the current approach causes TLE, we might consider combining self.find_max with DFS into a single traversal.

During the DFS traversal, we can maintain a `dp` structure to record the best subset sums for each node/state.

At each node (or level), we compute the optimal subset sum for all valid states (i.e., all possible combinations or constraints) and propagate that information up the tree.

After the DFS completes, we aggregate the best results from all nodes into the final answer `self.res`.

note. 

- state: since digits range from [0,9], we can use bitmask to save which digit has already existed in 10 bits

```
class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        mod = 1000000007

        n = len(vals)
        child = [[] for _ in range(n)]
        for node in range(1, n):
            child[par[node]].append(node)

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
```