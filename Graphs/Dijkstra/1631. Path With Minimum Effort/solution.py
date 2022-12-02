# Dijkstra: O(E log V), where E = 4*ROWS*COLS and V = ROWS*COLS
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        dp = [[inf] * COLS for _ in range(ROWS)]
        dp[0][0] = 0
        
        minH = [(0,0,0)] # row, col, effort
        while minH:
            r, c, effort = heapq.heappop(minH)

            if r == ROWS-1 and c == COLS-1:
                return effort

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0 <= row < ROWS and 0 <= col < COLS:
                    newEff = max(effort, abs(heights[row][col] - heights[r][c]))
                    if newEff < dp[row][col]:
                        dp[row][col] = newEff
                        heapq.heappush(minH, [row, col, newEff])
        return -1

# Binary Search + DFS: O(n*log(MAX_HEIGHT)) = O(ROWS*COLS*log(10**6))
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r, c, visited, k):
            if r == ROWS-1 and c == COLS-1: return True

            visited[r][c] = True
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if 0 <= row < ROWS and 0 <= col < COLS and not visited[row][col]:
                    if abs(heights[row][col]-heights[r][c]) <= k:
                        if dfs(row, col, visited, k): return True
            return False

        def canReachDest(threshold):
            visited = [[False] * COLS for _ in range(ROWS)]
            return dfs(0, 0, visited, threshold)

        l, r = 0, 10**6
        while l < r:
            mid = l + (r-l)//2
            if canReachDest(mid):
                r = mid
            else:
                l = mid+1
        return l