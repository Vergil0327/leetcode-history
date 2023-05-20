# a/b = a/aa * aa/b -> think this as a graph from a -> aa -> b
# use BFS to explore answer
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        results = defaultdict(lambda: -1)
        graph = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            results[(a,a)] = 1
            results[(b,b)] = 1
            results[(a,b)] = values[i]
            results[(b,a)] = 1 / values[i]

            graph[a].append(b)
            graph[b].append(a)
            
        def BFS(x, y):
            queue = deque([(x,y,1)])
            visited = set()
            while queue:
                for _ in range(len(queue)):
                    a, b, curr = queue.popleft()

                    if (a, b) in visited: continue
                    visited.add((a,b))

                    if (a,b) in results:
                        return results[(a,b)] * curr

                    for aa in graph[a]:
                        # a/b = a/aa * aa/b
                        if results[(a,aa)] == -1: continue
                        queue.append([aa,b,curr*results[(a,aa)]])
            return -1

        res = []
        for x, y in queries:
            if (x not in graph) or (y not in graph):
                res.append(-1)
            elif x == y:
                res.append(1)
            else:
                v = BFS(x, y)
                results[(x,y)] = v
                results[(y,x)] = 1/v
                res.append(v)
        return res