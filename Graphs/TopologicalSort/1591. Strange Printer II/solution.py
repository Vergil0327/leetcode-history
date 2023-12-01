# topological sort by BFS
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        coordinate = defaultdict(lambda :[n,0,m,0]) # left,right,top, bottom
        for i in range(m):
            for j in range(n):
                coordinate[targetGrid[i][j]][0] = min(coordinate[targetGrid[i][j]][0], j)
                coordinate[targetGrid[i][j]][1] = max(coordinate[targetGrid[i][j]][1], j)
                coordinate[targetGrid[i][j]][2] = min(coordinate[targetGrid[i][j]][2], i)
                coordinate[targetGrid[i][j]][3] = max(coordinate[targetGrid[i][j]][3], i)
        
        paintedColor = [[set() for _ in range(n)] for _ in range(m)]
        for color, (l, r, top, bot) in coordinate.items():
            for i in range(top, bot+1):
                for j in range(l, r+1):
                    paintedColor[i][j].add(color)

        graph = defaultdict(set)
        indeg = [-1]*61 # 1 <= targetGrid[row][col] <= 60
        for color in coordinate:
            indeg[color] = 0

        for i in range(m):
            for j in range(n):
                for nei in paintedColor[i][j]:
                    if nei == targetGrid[i][j]: continue
                    if targetGrid[i][j] in graph[nei]: continue

                    graph[nei].add(targetGrid[i][j])
                    indeg[targetGrid[i][j]] += 1

        queue = deque()
        for node, deg in enumerate(indeg):
            if deg == 0:
                queue.append(node)

        numColor = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                numColor += 1

                for nei in graph[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        queue.append(nei)
        return numColor == len(coordinate)

# topological sort by DFS
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        coordinate = defaultdict(lambda :[n,0,m,0]) # left,right,top, bottom
        for i in range(m):
            for j in range(n):
                coordinate[targetGrid[i][j]][0] = min(coordinate[targetGrid[i][j]][0], j)
                coordinate[targetGrid[i][j]][1] = max(coordinate[targetGrid[i][j]][1], j)
                coordinate[targetGrid[i][j]][2] = min(coordinate[targetGrid[i][j]][2], i)
                coordinate[targetGrid[i][j]][3] = max(coordinate[targetGrid[i][j]][3], i)
        
        paintedColor = [[set() for _ in range(n)] for _ in range(m)]
        for color, (l, r, top, bot) in coordinate.items():
            for i in range(top, bot+1):
                for j in range(l, r+1):
                    paintedColor[i][j].add(color)

        graph = defaultdict(set)
        for i in range(m):
            for j in range(n):
                for nei in paintedColor[i][j]:
                    if nei == targetGrid[i][j]: continue
                    if targetGrid[i][j] in graph[nei]: continue

                    graph[nei].add(targetGrid[i][j])
        
        visited = defaultdict(int)

        VALID, CYCLE = 1, 2
        def dfs(node):
            if visited[node] == VALID: return True

            visited[node] = CYCLE
            for nei in graph[node]:
                if visited[nei] == VALID: continue
                if visited[nei] == CYCLE: return False
                if not dfs(nei): return False

            visited[node] = VALID
            return True
        for color in coordinate:
            if not dfs(color): return False
        return True