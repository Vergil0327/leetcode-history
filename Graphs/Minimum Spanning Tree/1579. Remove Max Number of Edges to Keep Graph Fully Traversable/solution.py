class UnionFind:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.parent = [i for i in range(n+1)] # 1-based, i from 1 to n

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
        if px == py: return
        
        if px < py:
            parent[py] = px
        else:
            parent[px] = py
    
    def buildTree(self):
        find = self.find
        union = self.union
        
        cnt = 0
        used = []
        for typ, u, v in self.edges:
            if find(u) != find(v):
                union(u, v)
                cnt += 1
                used.append((typ, u, v))
        return used if cnt == self.n-1 else None
        

# time: O(nlogn)
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = []
        bob = []
        for edge in edges:
            typ = edge[0]
            if typ == 3:
                alice.append(edge)
                bob.append(edge)
            elif typ == 2:
                bob.append(edge)
            else:
                alice.append(edge)
        
        # we union type-3 edge first
        alice.sort(reverse=True)
        bob.sort(reverse=True)
        
        ufA = UnionFind(n, alice)
        usedEdgesA = ufA.buildTree()
        
        ufB = UnionFind(n, bob)
        usedEdgesB = ufB.buildTree()
        
        if usedEdgesA is None or usedEdgesB is None: return -1
        
        required = set(usedEdgesA) | set(usedEdgesB)
        return len(edges) - len(required)
