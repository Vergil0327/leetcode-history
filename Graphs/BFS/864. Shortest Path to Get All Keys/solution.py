class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])

        keys = set()
        start = [-1, -1, 0] # row, col, key we have
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start[0] = i
                    start[1] = j
                elif grid[i][j] >= "a" and grid[i][j] <= "f":
                    keys.add(grid[i][j])

        finalState = 0
        for key in keys:
            finalState |= (1<<(ord(key)-ord("a")))

        step = -1
        queue = deque([start])
        visited = [[set() for _ in range(n)] for _ in range(m)]
        visited[start[0]][start[1]].add(start[2])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            step += 1
            for _ in range(len(queue)):
                r, c, keyState = queue.popleft()

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row<0 or row >= m or col < 0 or col >= n: continue
                    if grid[row][col] == "#": continue
                    
                    if "A" <= grid[row][col] <= "F":
                        i = ord(grid[row][col])-ord("A")
                        if (keyState>>i)&1 == 0: continue

                    newKeyState = keyState
                    if "a" <= grid[row][col] <= "f":
                        newKeyState |= (1<<(ord(grid[row][col]) - ord("a")))

                    if newKeyState in visited[row][col]: continue
                    visited[row][col].add(newKeyState)

                    if newKeyState == finalState:
                        return step+1

                    queue.append([row, col, newKeyState])
        return -1