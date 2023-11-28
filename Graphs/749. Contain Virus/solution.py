class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        # area: [即將傳染地區, 感染地區, boundary wall count]
        def dfs(r, c, visited, area):
            if visited[r][c]: return
            if isInfected[r][c] == 0:
                area[2] += 1 # wall count
                area[0].add((r, c))
                return

            # 傳染地
            visited[r][c] = 1
            area[1].add((r,c))

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= m or col < 0 or col >= n: continue
                if isInfected[row][col] == -1: continue # 已封鎖
                dfs(row, col, visited, area)            

        res = 0
        for _ in range(m*n):
            visited = [[0]*n for _ in range(m)]
            
            pq = [] # max heap
            for i in range(m):
                for j in range(n):
                    if not visited[i][j] and isInfected[i][j] == 1:
                        area = [set(), set(), 0] # [即將傳染地區, 感染地區, boundary wall count]
                        dfs(i, j, visited, area)
                        heapq.heappush(pq, [-len(area[0]), area]) # 以即將傳染地區數量作為key

            if not pq: break # 全面封鎖

            # quarantine infected area and update required walls
            _, (danger_area, infected_area, wall_cnt) = heapq.heappop(pq)
            for i, j in infected_area:
                isInfected[i][j] = -1
            res += wall_cnt

            # 剩下沒封鎖的地區開始傳染
            while pq:
                _, (danger_area, _, _) = heapq.heappop(pq)
                for i, j in danger_area:
                    isInfected[i][j] = 1

        return res
