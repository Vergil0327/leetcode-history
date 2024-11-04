class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque([[0,0]]) # r, c
        visited = [[inf]*n for _ in range(m)]
        visited[0][0] = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    row, col = r+dr, c+dc
                    if row<0 or row>=m or col<0 or col>=n: continue
                    if visited[row][col] <= visited[r][c]+1: continue
                    visited[row][col] = min(visited[row][col], max(visited[r][c], moveTime[row][col])+1)
                    queue.append([row, col])

        return visited[m-1][n-1]