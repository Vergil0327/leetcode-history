class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        SET = set()
        def dfs(state, i):
            if state: SET.add(state)
            if i == len(tiles): return

            dfs(state, i+1)
            for j in range(len(state)+1):
                dfs(state[:j] + tiles[i] + state[j:], i+1)

        dfs("", 0)
        return len(SET)
