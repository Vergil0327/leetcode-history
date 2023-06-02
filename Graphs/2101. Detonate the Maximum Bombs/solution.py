class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                manhattan = (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2
                if manhattan <= bombs[i][2]**2:
                    graph[i].append(j)
                if manhattan <= bombs[j][2]**2:
                    graph[j].append(i)

        def dfs(node, visited):
            if node in visited: return 0
            visited.add(node)

            res = 1
            for nei in graph[node]:
                res += dfs(nei, visited)
            return res

        res = 1
        for i in range(n):
            cnt = dfs(i, set())
            res = max(res, cnt)
        return res