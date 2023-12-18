class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        queue = deque()
        player = [-1, -1]
        box = [-1, -1]
        target = [-1, -1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "B":
                    box = (i, j)
                elif grid[i][j] == "S":
                    player = (i, j)
                elif grid[i][j] == "T":
                    target = (i, j)

        queue.append([box, player]) # box_pos, player_pos
        visited = set()
        visited.add((box[0], box[1], player[0], player[1]))

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def check_player_reachable(src, dst, box_pos):
            q = deque([src])
            seen = set()
            while q:
                i, j = q.popleft()
                if i == dst[0] and j == dst[1]: return True
                for di, dj in dirs:
                    ii, jj = i+di, j+dj
                    if ii < 0 or ii >= m or jj < 0 or jj >= n: continue
                    if grid[ii][jj] == "#": continue
                    if ii == box_pos[0] and jj == box_pos[1]: continue
                    if (ii, jj) in seen: continue
                    seen.add((ii, jj))
                    q.append((ii, jj))
            return False

        push = 0
        while queue:
            for _ in range(len(queue)):
                (r, c), player_pos = queue.popleft()

                if (r, c) == target:
                    return push

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    player_next = (r-dr, c-dc)

                    if row < 0 or row >= m or col < 0 or col >= n: continue
                    if player_next[0] < 0 or player_next[0] >= m or player_next[1] < 0 or player_next[1] >= n: continue
                    if grid[row][col] == "#": continue
                    if grid[player_next[0]][player_next[1]] == "#": continue

                    if (row, col, player_next[0], player_next[1]) in visited:continue

                    if check_player_reachable(player_pos, player_next, (r,c)):
                        visited.add((row, col, player_next[0], player_next[1]))
                        queue.append([(row, col), (r, c)])
            push += 1
        return -1
