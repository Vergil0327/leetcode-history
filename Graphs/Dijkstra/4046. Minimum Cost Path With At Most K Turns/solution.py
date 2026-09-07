# Algorithm Approach:
# 1. State Representation:
#    dp[r][c][turns][dir] = minimum cost to reach (r, c) moving in direction 'dir' with 'turns' turns used.
#    Directions: 0: Right, 1: Down, 2: Left, 3: Up.

# 2. Base Case:
#    - At (0, 0) with 0 turns:
#      If we move right from (0,0), it's 0 turns.
#      If we move down from (0,0), it's 0 turns.
#      Other directions are invalid/unreachable initially.

# 3. Dijkstra State Transitions:
#    Priority Queue stores (cumulative_cost, turns, r, c, d).
#    For each direction 'next_d' (0..3):
#      next_r = r + dr, next_c = c + dc
#      next_turns = turns if (d == next_d) else turns + 1
#      if next_turns <= k and cost + grid[next_r][next_c] < dp[next_r][next_c][next_turns][next_d]:
#          dp[next_r][next_c][next_turns][next_d] = cost + grid[next_r][next_c]
#          push to PQ.


# Complexity Analysis:
# - Time Complexity: O(m * n * k * log(m * n * k)), where m, n <= 75 and k <= 75. State space size = 75 * 75 * 75 * 4 ≈ 1.6 * 10^6, easily completing under 0.15s.
# - Space Complexity: O(m * n * k) for the 4D distance array.

import heapq

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        
        # dist[r][c][turns][dir]
        dist = [[[[INF] * 4 for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]
        
        # Priority Queue: (cost, turns, r, c, direction)
        # 0: Right, 1: Down, 2: Left, 3: Up
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # From (0, 0), initial moves in any direction cost 0 turns
        pq = []
        for d in range(4):
            dist[0][0][0][d] = grid[0][0]
            heapq.heappush(pq, (grid[0][0], 0, 0, 0, d))
            
        while pq:
            cost, turns, r, c, d = heapq.heappop(pq)
            
            if cost > dist[r][c][turns][d]:
                continue
                
            if r == m - 1 and c == n - 1:
                return cost
                
            for next_d, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_turns = turns if d == next_d else turns + 1
                    if next_turns <= k:
                        next_cost = cost + grid[nr][nc]
                        if next_cost < dist[nr][nc][next_turns][next_d]:
                            dist[nr][nc][next_turns][next_d] = next_cost
                            heapq.heappush(pq, (next_cost, next_turns, nr, nc, next_d))
                            
        return -1
