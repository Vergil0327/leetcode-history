class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        graph = defaultdict(list)

        for start, end in pairs:
            indegree[end] += 1
            outdegree[start] += 1
            graph[start].append(end)

        start = -1
        for node in graph:
            # outdegree = indegree + 1 => start node of Eulerian Path
            if outdegree[node] - indegree[node] == 1:
                start = node
        if start == -1: # we can choose any node as start
            start = pairs[0][0]

        def findEulerianPath(start):
            path = [] # start, end, start, end, start, end, ...
            def dfs(start, path):
                while graph[start]:
                    nxt = graph[start].pop()
                    dfs(nxt, path)
                path.append(start)
            dfs(start, path)
            path.reverse()
            return path

        path = findEulerianPath(start)

        res = []
        for i in range(0, len(path)-1):
            res.append([path[i], path[i+1]])
        return res