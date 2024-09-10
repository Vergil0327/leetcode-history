class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        dirs = [[2, -1], [2, 1], [-2, -1], [-2, 1], [-1, 2], [1, 2], [-1, -2], [1, -2]]

        n = len(positions)
        positions = positions + [[kx, ky]]

        minSteps = [[0]*(n+1) for _ in range(n+1)]
        def bfs(i, j):
            queue = deque([positions[i]])
            visited = set()
            step = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    if [r,c] == positions[j]: return step

                    for dr, dc in dirs:
                        row, col = r+dr, c+dc
                        if row < 0 or row >= 50 or col < 0 or col >= 50: continue
                        if (row, col) in visited: continue
                        visited.add((row, col))
                        queue.append([row, col])
                step += 1
            return step

        for i in range(n+1):
            for j in range(i-1, -1, -1):
                minSteps[i][j] = minSteps[j][i] = bfs(i, j)

        @cache
        def dfs(i, state, isAlice):
            if state == (1<<n)-1: return 0

            res = 0 if isAlice else inf
            for j in range(n):
                if (state>>j)&1: continue
                if isAlice:
                    res = max(res, dfs(j, state | (1<<j), 1-isAlice) + minSteps[i][j])
                else:
                    res = min(res, dfs(j, state | (1<<j), 1-isAlice) + minSteps[i][j])
            return res

        return dfs(n, 0, 1)
