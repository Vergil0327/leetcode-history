# BFS + Min Heap
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        
        minH = [] # [height, x, y]
        for y in range(m):
            for x in range(n):
                if y == 0 or y == m-1 or x == 0 or x == n-1:
                    heapq.heappush(minH, [heightMap[y][x], y, x])

        # start from border to floodfill
        visited = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        seaLevel = -inf # or see it as wall height
        trapped = 0
        while minH:
            currHei, y, x = heapq.heappop(minH)
            seaLevel = max(seaLevel, currHei)

            if (currHei, y, x) in visited: continue
            visited.add((currHei, y, x))

            trapped += seaLevel - heightMap[y][x]

            for dy, dx in dirs:
                nxtY, nxtX = y+dy, x+dx
                if not (nxtY >= 0 and nxtY < m and nxtX >= 0 and nxtX < n): continue
                if (heightMap[nxtY][nxtX], nxtY, nxtX) in visited: continue
                heapq.heappush(minH, [heightMap[nxtY][nxtX], nxtY, nxtX])

        return trapped

# DFS + minHeap
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        
        border = [] # [height, x, y]
        for y in range(m):
            for x in range(n):
                if y == 0 or y == m-1 or x == 0 or x == n-1:
                    heapq.heappush(border, [heightMap[y][x], y, x])

        wallHeight = 0
        visited = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(y, x, wallHeight):
            if (y, x) in visited: return 0
            visited.add((y,x))

            water = wallHeight - heightMap[y][x]
            for dy, dx in dirs:
                nxtY, nxtX = y+dy, x+dx
                if not (nxtY >= 0 and nxtY < m and nxtX >= 0 and nxtX < n): continue
                if heightMap[nxtY][nxtX] < wallHeight:
                    water += dfs(nxtY, nxtX, wallHeight)
                else:
                    heapq.heappush(border, [heightMap[nxtY][nxtX], nxtY, nxtX])
            return water

        trapped = 0
        while border:
            hei, y, x = heapq.heappop(border)
            wallHeight = max(wallHeight, hei)
            trapped += dfs(y, x, wallHeight)
        return trapped