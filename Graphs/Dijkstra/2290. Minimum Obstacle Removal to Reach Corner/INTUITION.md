# Intuition

一開始想法是從左上(0,0)empty cell出發, 再利用BFS逐步將四周利用union-find連通起來
直到左上跟右下位置在同個union-find group裡
```py
def minimumObstacles(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    parent = list(range(m*n))
    rank = [1]*(m*n)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py: return False
        if rank[px] <= rank[py]:
            parent[px] = py
            rank[py] += rank[px]
        else:
            parent[py] = px
            rank[px] += rank[py]
        return True
    
    def toKey(row, col):
        return row*n + col
    
    def toPos(key):
        return key//n, key%n

    pq = [[0, 0, 0]] # [remove, row, col]
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    while pq:
        rm, r, c = heapq.heappop(pq)
        if find(toKey(r, c)) == find(toKey(m-1, n-1)):
            return rm

        for dr, dc in dirs:
            row, col = r+dr, c+dc
            if row < 0 or row >= m or col < 0 or col >= n: continue
            if union(toKey(r, c), toKey(row, col)):
                if grid[row][col] == 1:
                    heapq.heappush(pq, [rm+1, row, col])
                else:
                    heapq.heappush(pq, [rm, row, col])
                    
    return 0
```

但這樣一看會發現這其實就是個dijkstra:
- grid[i][j].cost == 1 if grid[i][j] == 1
- grid[i][j].cost == 0 if grid[i][j] == 0

直接用dijkstra algorithm即可