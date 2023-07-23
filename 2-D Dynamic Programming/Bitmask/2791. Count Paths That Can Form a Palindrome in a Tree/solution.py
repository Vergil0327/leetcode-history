class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        @lru_cache(None)
        def dfs(node):
            if node <= 0: return 0
            return dfs(parent[node]) ^ (1<<(ord(s[node]) - ord("a")))
        
        n = len(parent)
        res = 0
        dp = defaultdict(int)
        for node in range(n):
            parities = dfs(node)

            # palindrome consist of current path with another path whose parity is same us current path
            res += dp[parities]
            # palindrome consist of current node_to_root path + another path
            for i in range(26):
                res += dp[parities ^ (1<<i)]

            dp[parities] += 1
            
        return res
