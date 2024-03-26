class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod = 10**9 + 7
        
        n = len(prevRoom)
        graph = defaultdict(list)
        for i in range(n):
            graph[prevRoom[i]].append(i)

        def dfs(i):
            if len(graph[i]) == 0: # leaf nodes
                return 1, 1 # (number of ways, number of nodes)
            
            res = 1
            x = 0
            for nxt in graph[i]:
                ways, y = dfs(nxt)
                res = (res * ways * math.comb(x+y, y)) % mod
                x += y

            return res%mod, x + 1
        return dfs(0)[0]


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod = 10**9 + 7
        
        n = len(prevRoom)
        graph = defaultdict(list)
        for i in range(n):
            graph[prevRoom[i]].append(i)

        fac = [1] * (n+1)
        fac_inv = [1] * (n+1)
        for i in range(2, len(fac)):
            fac[i] = fac[i-1]*i%mod
            fac_inv[i] = pow(fac[i], mod-2, mod)

        def dfs(i):
            if len(graph[i]) == 0: # leaf nodes
                return 1, 1 # (number of ways, number of nodes)
            
            res = 1
            x = 0
            for nxt in graph[i]:
                ways, y = dfs(nxt)
                comb =  (((fac[x+y] * fac_inv[x]) % mod) * fac_inv[y]) % mod
                res = (res * ways % mod) * comb % mod
                x += y

            return res, x + 1

        return dfs(0)[0]