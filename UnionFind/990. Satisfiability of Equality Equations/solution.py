class Solution:
    def equationsPossible(self, eqs: List[str]) -> bool:
        parent = [i for i in range(26)]
        rank = [1] * 26
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            
            if rank[px] >= rank[py]:
                rank[px] += rank[py]
                parent[py] = px
            else:
                rank[py] += rank[px]
                parent[px] = py
            return True
        
        def isConnected(x, y):
            return find(x) == find(y)
        
        # union first, then check validity
        offset = ord("a")

        # union
        for eq in eqs:
            x, y = ord(eq[0])-offset, ord(eq[3])-offset
            if eq[1] == "=":
                union(x, y)
        
        # check
        # one-line: not any(eq[1] == "!" and isConnected(eq[0], eq[3]) for eq in eqs)
        for eq in eqs:
            x, y = ord(eq[0])-offset, ord(eq[3])-offset
            if eq[1] == "!":
                if isConnected(x, y): return False

        return True

#         union-find
#         if eqs[i][1] == "=":
#             union(eqs[i][0], eqs[i][3])
        
#         if eqs[i][1] == "!":
#             return not isConnected(eqs[i][0], eqs[i][3])