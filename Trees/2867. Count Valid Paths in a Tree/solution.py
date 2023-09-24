class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        if n == 1: return 0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        
        isPrime = [0, 0] + [1] * (n-1)
        for i in range(2, int(math.sqrt(n))+1):
            if not isPrime[i]: continue
            # all the factors before i*i have been considered at i-1, i-2, ..., 3, 2
            for j in range(i*i, n+1, i):
                isPrime[j] = 0
        
        self.res = 0
        def dfs(node, prev):
            # not_prime, prime
            res = [0, 1] if isPrime[node] else [1, 0]

            for nei in graph[node]:
                if nei == prev: continue

                x, y = dfs(nei, node)
                self.res += res[0]*y + res[1]*x
                if isPrime[node]:
                    res[1] += x
                else:
                    res[0] += x
                    res[1] += y
                
            return res[0], res[1]
            
        dfs(1, -1)
        return self.res