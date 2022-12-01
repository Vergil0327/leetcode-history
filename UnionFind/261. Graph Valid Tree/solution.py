# n = 5
# edges = [[0,1], [0,2], [0,3], [1,4]]

class Solution:
    def graphValidTree(self, n: int, edges: List[List[int]]):
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py : return False
            parent[px] = py

        connected = 0
        for u, v in edges:
            if not union(u, v): return False
            connected += 1

        # we can't directly return True because it might exists some orphan node
        return connected == n-1