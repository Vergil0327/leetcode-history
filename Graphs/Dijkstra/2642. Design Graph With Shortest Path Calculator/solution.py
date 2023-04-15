class Graph:

    def __init__(self, n: int, edges: List[List[int]]):        
        self.graph = graph = defaultdict(list)
        for u, v, c in edges:
            graph[u].append([v, c])


    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append([edge[1], edge[2]])
                    

    def shortestPath(self, node1: int, node2: int) -> int:
        minH = [[0, node1]]
        graph = self.graph
        
        visited = set()
        while minH:
            cost, curr = heapq.heappop(minH)
            if curr == node2: return cost
            
            if curr in visited: continue
            visited.add(curr)
            
            for nei, c in graph[curr]:
                heapq.heappush(minH, [cost+c, nei])
        return -1
