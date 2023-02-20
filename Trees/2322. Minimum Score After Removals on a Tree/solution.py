# Python nearly TLE
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # calculate XOR of whole tree
        def dfs(node, parent):
            xor = nums[node]
            for nei in graph[node]:
                if nei == parent: continue
                xor ^= dfs(nei, node)
            return xor

        self.res = inf
        def calScore(node, parent, totalU, totalV):
            xor = nums[node]
            for nei in graph[node]:
                if nei == parent: continue
                subtreeXor = calScore(nei, node, totalU, totalV)
                otherHalf = totalU^subtreeXor
                MAX = max(totalV, max(otherHalf, subtreeXor))
                MIN = min(totalV, min(otherHalf, subtreeXor))
                if MAX-MIN < self.res:
                    self.res = MAX-MIN

                xor ^= subtreeXor
            return xor

        for u, v in edges:
            # first cut, cut u-v
            graph[u].remove(v)
            graph[v].remove(u)

            totalXorU, totalXorV = dfs(u, u), dfs(v, v)
            calScore(u, u, totalXorU, totalXorV)
            calScore(v, v, totalXorV, totalXorU)

            # restore u-v edge
            graph[u].add(v)
            graph[v].add(u)
        return self.res
    
# Slightly Better
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        overallXOR = 0
        for num in nums:
            overallXOR ^= num
        
        # calculate XOR of whole tree
        def dfs(node, parent):
            xor = nums[node]
            for nei in graph[node]:
                if nei == parent: continue
                xor ^= dfs(nei, node)
            return xor

        self.res = inf
        def calScore(node, parent, totalU, totalV):
            xor = nums[node]
            for nei in graph[node]:
                if nei == parent: continue
                subtreeXor = calScore(nei, node, totalU, totalV)
                otherHalf = totalU^subtreeXor
                MAX = max(totalV, max(otherHalf, subtreeXor))
                MIN = min(totalV, min(otherHalf, subtreeXor))
                if MAX-MIN < self.res:
                    self.res = MAX-MIN

                xor ^= subtreeXor
            return xor

        for u, v in edges:
            # first cut, cut u-v
            graph[u].remove(v)
            graph[v].remove(u)

            # totalXorU, totalXorV = dfs(u, u), dfs(v, v)
            totalXorU = dfs(u, u)
            totalXorV = overallXOR^totalXorU
            calScore(u, u, totalXorU, totalXorV)
            calScore(v, v, totalXorV, totalXorU)

            # restore u-v edge
            graph[u].add(v)
            graph[v].add(u)
        return self.res
    

# Optimzed, with cache

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        xor = [0] * len(nums)
        def getXor(node,parent):
            xor[node] = nums[node]
            for child in graph[node]:
                if child == parent:
                    continue
                
                xor[node] ^= getXor(child,node) 
            return xor[node]
        
        parent = defaultdict(set)
        def dfs(node,p):
            parent[node] = set([node])
            for child in graph[node]:
                if child == p:
                    continue
                
                parent[node] |= dfs(child,node)
            
            return parent[node]
        getXor(0,-1)
        dfs(0,-1)

        res = float('inf')
        for rootA in range(1,len(nums)):
            for rootB in range(rootA+1, len(nums)):
                
                if rootB in parent[rootA]:
                    a = xor[0] ^ xor[rootA]
                    b = xor[rootA] ^ xor[rootB]
                    c = xor[rootB]
                    res = min(res,max(a,b,c) - min(a,b,c)) 
                elif rootA in parent[rootB]:
                    a = xor[0] ^ xor[rootB]
                    b = xor[rootB] ^ xor[rootA]
                    c = xor[rootA]
                    res = min(res,max(a,b,c) - min(a,b,c)) 
                else:
                    a = xor[0] ^ xor[rootA] ^ xor[rootB]
                    b = xor[rootA]
                    c = xor[rootB]
                    res = min(res,max(a,b,c) - min(a,b,c)) 
        return res