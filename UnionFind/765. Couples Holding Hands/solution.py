# Union-Find
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        couch = {} # {couple: couchID}, couchID from 0 to N-1
        for i, v in enumerate(row):
            couch[v] = i//2
        
        n = len(row)
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            px, py = find(x), find(y)
            parent[py] = px
        
        swap = 0
        for couple in range(0, n-1, 2):
            a = couch[couple]
            b = couch[couple+1]
            if find(a) != find(b):
                union(a, b)
                swap += 1
        return swap
#    0      1
# [0, 2], [1, 3]
# ---------
#     ---------
    
#    0      1
# [3, 2], [0, 1]
# ------  ------


#    0      1       2
# [0, 2], [1, 4], [3, 5]
# ---------   ---------
#     --------------
# [0,1],[1,2],[0,2]