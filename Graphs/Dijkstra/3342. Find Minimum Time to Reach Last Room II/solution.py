class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        pq = [[0,0,0,0]] # t, alternating, r, c
        visited = set([(0,0)])
        while pq:
            t, alt, r, c = heapq.heappop(pq)
            if r == m-1 and c == n-1:
                return t
            
            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row<0 or row>=m or col<0 or col>=n: continue
                if (row, col) in visited: continue
                visited.add((row, col))
                tt = max(t, moveTime[row][col])+1+alt
                heapq.heappush(pq, [tt, 1-alt, row, col])
        return -1
