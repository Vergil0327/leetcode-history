# 後續新增test cases後會TLE

Trie = lambda: defaultdict(Trie)
IS_END = "ISEND"
COST = "COST"

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        tri = Trie()
        for word, cost in zip(words, costs):
            root = tri
            for ch in word:
                root = root[ch]
            root[IS_END] = True
            root[COST] = cost if COST not in root else min(root[COST], cost)

        n = len(target)
        dp = [-1] * n
        def dfs(i):
            if i == n: return 0
            
            if dp[i] == -1:
                dp[i] = inf
                root = tri
                for j in range(i, n):
                    if target[j] not in root: break
                    root = root[target[j]]
                    if root[IS_END]:
                        dp[i] = min(dp[i], dfs(j+1) + root[COST])
            return dp[i]

        res = dfs(0)
        return res if res < inf else -1