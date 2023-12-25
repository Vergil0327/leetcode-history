class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indeg = [0] * n
        for u, v in edges:
            if u == v: return -1 # got self-cycle
            graph[u].append((v, colors[v]))
            indeg[v] += 1

        res = 0
        dp = [defaultdict(int) for _ in range(n)]
        queue = deque()
        for node, deg in enumerate(indeg): # node, color
            if deg == 0:
                queue.append([node, colors[node]])
                dp[node][colors[node]] = 1
                res = 1

        numNodes = 0
        while queue:
            
            for _ in range(len(queue)):
                node, color_node = queue.popleft()
                numNodes += 1

                for nei, color_nei in graph[node]:
                    for color in "abcdefghijklmnopqrstuvwxyz":
                        dp[nei][color] = max(dp[nei][color], dp[node][color] + (1 if color == color_nei else 0))
                    res = max(res, dp[nei][color_nei])

                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        queue.append([nei, color_nei])

        if numNodes != n: return -1 # got cycle

        return res
    
# Neetcode: https://www.youtube.com/watch?v=xLoDjKczUSk
class Solution_DFS:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            if u == v: return -1 # got self-cycle
            graph[u].append((v, colors[v]))

        res = 0
        n = len(colors)
        visited = set() # memorize have we done this node before
        path = set() # detect cycle
        count = [[0] * 26 for _ in range(n)] # count[node][color]: maximum number of color until node

        def dfs(node):
            if node in path: return inf # found cycle
            if node in visited: return 0

            path.add(node)
            visited.add(node)

            color = ord(colors[node]) - ord("a")
            count[node][color] = 1

            for nei in graph[node]:
                if dfs(nei) == inf: return inf
                for c in range(26):
                    count[node][c] = max(
                        count[node][c],
                        count[nei][c] + (1 if c == color else 0)
                    )
            
            path.remove(node)
            return max(count[node])

        for node in range(n):
            res = max(res, dfs(node))
        return res if res != inf else -1
    
# concise way to implement topological sort with DFS
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            if u == v: return -1 # self-cycle
            graph[u].append(v)

        n = len(colors)
        visited = defaultdict(int)
        dp = [[0]*26 for _ in range(n)]
        RESOLVE, VISITED = 1, 2

        def dfs(node):
            if visited[node] == VISITED: return inf
            if visited[node] == RESOLVE: return 0

            visited[node] = VISITED

            color = ord(colors[node]) - ord("a")
            dp[node][color] = 1
            for nei in graph[node]:
                if dfs(nei) == inf: return inf
                for c in range(26):
                    dp[node][c] = max(dp[node][c], dp[nei][c] + (1 if c == color else 0))

            visited[node] = RESOLVE

            return max(dp[node])

        res = max(dfs(node) for node in range(n))
        return res if res != inf else -1