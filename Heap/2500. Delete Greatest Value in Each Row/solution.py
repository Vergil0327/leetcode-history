# max heap
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        heaps = []
        for r in range(ROWS):
            h = []
            for c in range(COLS):
                h.append(-grid[r][c])
            heapq.heapify(h)
            heaps.append(h)
        
        res = 0
        for _ in range(COLS):
            val = 0
            for h in heaps:
                v = -heapq.heappop(h)
                val = max(val, v)
            res += val
        return res