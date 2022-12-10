class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not edges: return max(vals)

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        maxSum = 0
        for i in range(len(vals)):
            values = []
            for nei in graph[i]:
                if vals[nei] > 0:
                    values.append(vals[nei])
            values.sort(reverse=True)
            
            maxSum = max(maxSum, vals[i]+sum(values[:k]))
        return maxSum
