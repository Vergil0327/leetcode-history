class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        parent = [-1] * len(nums)
        @lru_cache(None)
        def dfs(node, inverted, lastInvertDist):
            # don't invert
            res = nums[node] * inverted
            inverted_res = nums[node] * inverted * -1
            for nxt in graph[node]:
                if nxt == parent[node]: continue
                parent[nxt] = node
                res += dfs(nxt, inverted, min(k, lastInvertDist+1))

                # can invert
                # should check if distance since last inverted parent is at least k
                if lastInvertDist >= k:
                    inverted_res += dfs(nxt, inverted*-1, 1)
            
            return max(res, inverted_res) if lastInvertDist >= k else res
        dfs.cache_clear()
        return dfs(0,1,k)

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        graph = defaultdict(list)
        n = len(nums)
        graph = [[] for _ in range(n)]
        for node, nxt in edges:
            graph[node].append(nxt)
            graph[nxt].append(node)
        
        children = [[] for _ in range(n)]
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for nxt in graph[node]:
                    if not visited[nxt]:
                        queue.append(nxt)
                        children[node].append(nxt)
                        visited[nxt] = True
        
        @lru_cache(None)
        def dfs(node, inverted, lastInvertDist):
            # don't invert
            res = nums[node] * inverted
            inverted_res = nums[node] * inverted * -1
            for nxt in children[node]:
                res += dfs(nxt, inverted, min(k, lastInvertDist+1))

                # can invert
                # should check if distance since last inverted parent is at least k
                if lastInvertDist >= k:
                    inverted_res += dfs(nxt, inverted*-1, 1)
            
            return max(res, inverted_res) if lastInvertDist >= k else res
        dfs.cache_clear()
        return dfs(0,1,k)