import heapq

class Solution:
    def minCost(self, m: int, n: int, penalty: list[list[int]]) -> int:
        # dist[r][c][p] 記錄到達 (r, c) 且當前奇偶性為 p 時的最少花費
        # p = 1 代表下一次是奇數次行動 (Odd)
        # p = 0 代表下一次是偶數次行動 (Even)
        dist = [[[float('inf')] * 2 for _ in range(n)] for _ in range(m)]
        
        # 初始站在 (0, 0)，付第一個進入成本 1，下一次行動是 Action 1 (p = 1)
        dist[0][0][1] = 1
        
        # 優先佇列 (min-heap): (cost, r, c, p)
        pq = [(1, 0, 0, 1)]
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while pq:
            d, r, c, p = heapq.heappop(pq)
            
            # 找到終點即可直接回傳（Dijkstra 屬性）
            if r == m - 1 and c == n - 1:
                return d
            
            # 若不是最短路徑則跳過
            if d > dist[r][c][p]:
                continue
            
            next_p = 1 - p
            
            # 選擇 1：在原地等待 (Wait)
            wait_cost = d + penalty[r][c]
            if wait_cost < dist[r][c][next_p]:
                dist[r][c][next_p] = wait_cost
                heapq.heappush(pq, (wait_cost, r, c, next_p))
            
            # 選擇 2：向四個方向移動
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < m and 0 <= col < n:
                    # 判斷是否為當前 parity 允許的方向
                    # p == 1 (Odd): 允許 Down (1, 0) 與 Right (0, 1)
                    # p == 0 (Even): 允許 Up (-1, 0) 與 Left (0, -1)
                    is_parity_move = (p == 1 and (dr, dc) in ((1, 0), (0, 1))) or \
                                     (p == 0 and (dr, dc) in ((-1, 0), (0, -1)))
                    
                    entry_cost = (row + 1) * (col + 1)
                    extra_penalty = 0 if is_parity_move else penalty[r][c]
                    move_cost = d + entry_cost + extra_penalty
                    
                    if move_cost < dist[row][col][next_p]:
                        dist[row][col][next_p] = move_cost
                        heapq.heappush(pq, (move_cost, row, col, next_p))
                        
        return -1