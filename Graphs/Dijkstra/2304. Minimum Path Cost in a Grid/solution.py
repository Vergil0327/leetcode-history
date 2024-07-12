class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        pq = [[grid[0][j], 0, j] for j in range(n)]
        heapq.heapify(pq)
        seen = set()
        while pq:
            cost, i, j = heapq.heappop(pq)
            if i == m-1: return cost
            if (i, j) in seen: continue
            seen.add((i, j))

            for jj in range(n):
                heapq.heappush(pq, [cost + moveCost[grid[i][j]][jj] + grid[i+1][jj], i+1, jj])
        return 0