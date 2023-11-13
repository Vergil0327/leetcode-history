class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)

        coprimes = [set() for _ in range(51)]
        for num in range(1, 51):
            for other in range(1, 51):
                if gcd(num, other) == 1:
                    coprimes[num].add(other)

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        num2idx = [[] for _ in range(51)] # {ancestor's num: ancestor's level}
        ancestors = [] # {level: ancestor}
        
        res = [-1]*n
        def dfs(node, prev, level):
            idx = -1
            for p in coprimes[nums[node]]:
                if num2idx[p]:
                    idx = max(idx, num2idx[p][-1])

            if idx != -1:
                res[node] = ancestors[idx]
            
            num2idx[nums[node]].append(level)
            ancestors.append(node)

            for nei in graph[node]:
                if nei == prev: continue
                dfs(nei, node, level+1)

            # backtracking
            num2idx[nums[node]].pop()
            ancestors.pop()
        dfs(0, -1, 0)

        return res
