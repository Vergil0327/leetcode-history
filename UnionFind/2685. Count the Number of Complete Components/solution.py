class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = [[False]*n for _ in range(n)]
        for i in range(n):
            connected[i][i] = True
        
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in edges:
            connected[u][v] = True
            connected[v][u] = True
            
            pu, pv = find(u), find(v)
            if pu == pv: continue
                
            if pu < pv:
                parent[pv] = pu
            else:
                parent[pu] = pv
            
        groups = defaultdict(list)
        for node in range(n):
            groups[find(parent[node])].append(node)

        res = 0
        for components in groups.values():
            m = len(components)

            valid = True
            for i in range(m):
                x = components[i]
                for j in range(m):
                    y = components[j]
                    if connected[x][y] == False:
                        valid = False
                        break
                if not valid: break
            if not valid: continue
            res += 1
        return res

# Optimized
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:        
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u, v in edges:            
            pu, pv = find(u), find(v)
            if pu == pv: continue
                
            if pu < pv:
                parent[pv] = pu
            else:
                parent[pu] = pv

        groups = defaultdict(int)
        for node in range(n):
            groups[find(parent[node])] += 1

        edge = [0] * n
        for u, v in edges:
            edge[find(u)] += 1

        res = 0
        for group in groups:
            n = groups[group]
            if edge[group] == n*(n-1)//2:
                res += 1
            
        return res