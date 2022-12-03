class Kruskal:
    def __init__(self, n, edges, skip:int=None):
        self.n = n
        self.parent = [i for i in range(n)]
        self.edges = edges
        self.weight = None
        self.used = []
        self.skip = skip

    def find(self, x):
        parent = self.parent
        find = self.find
        
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(self, x, y):
        parent = self.parent
        find = self.find
        
        px, py = find(x), find(y)
        if px <= py:
            parent[py] = px
        else:
            parent[px] = py
    
    def getMin(self):
        edges = self.edges
        find = self.find
        union = self.union
        skip = self.skip
        
        weight = 0
        connected = 0

        for i, edge in enumerate(edges):
            if skip is not None and i == skip: continue
            u, v, w, original_idx = edge
            if find(u) != find(v):
                weight += w
                union(u, v)
                connected += 1

        # we need to check if it's a valid minimum spanning tree
        if connected == self.n-1: # connect n-1 times for n node
            return weight
        else:
            return float("inf")

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [edge + [i] for i, edge in enumerate(edges)] # store original index
        edges.sort(key=lambda x:x[2]) # sorted by weight
        
        k = Kruskal(n, edges)
        minCost = k.getMin()
        critical = set()
        for skip in range(len(edges)):
            k = Kruskal(n, edges, skip)
            if k.getMin() > minCost:
                critical.add(edges[skip][3])
            
        nonCritical = set()
        for skip in range(len(edges)):
            if edges[skip][3] in critical: continue

            edge = edges[skip]
            edges.insert(0, edge)
            k = Kruskal(n, edges, None)
            if k.getMin() == minCost:
                nonCritical.add(edge[3])
            edges.pop(0)
        
        return [list(critical), list(nonCritical)]
