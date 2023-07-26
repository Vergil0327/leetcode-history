class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        n = len(bottom)

        pattern = defaultdict(set)
        for s in allowed:
            pattern[s[:2]].add(s[2])

        @lru_cache(None)
        def dfs(bot, i, nxtLv):
            level = len(bot)
            if level == 1: return True

            if i == level-1:
                return dfs(nxtLv, 0, "")

            for top in pattern[bot[i:i+2]]:
                if dfs(bot, i+1, nxtLv+top): return True
            return False

        return dfs(bottom, 0, "")
