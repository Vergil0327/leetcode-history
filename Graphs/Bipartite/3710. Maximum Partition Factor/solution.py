
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        def isBipartite(exclusive: List[List[int]]) -> bool:
            group = [0] * len(exclusive)
            visited = set()
            def dfs(node):
                for nei in range(n):
                    if exclusive[node][nei]:    
                        if nei in visited:
                            if group[nei] == group[node]: return False
                            continue
                        visited.add(nei)

                        group[nei] = 1 - group[node]
                        if not dfs(nei): return False
                return True

            for node, _ in enumerate(exclusive):
                if node in visited: continue
                visited.add(node)

                if not dfs(node): return False
            return True

        def check(threshold):
            exclusive = [[0]*n for _ in range(n)]
            for i in range(n):
                row1, col1 = points[i]
                for j in range(i+1, n):
                    row2, col2 = points[j]
                    if abs(row2-row1) + abs(col2-col1) < threshold:
                        exclusive[i][j] = 1
                        exclusive[j][i] = 1
            return isBipartite(exclusive)
    
        l, r = 0, 10**9
        while l < r:
            mid = r - (r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l if l < 10**9 else 0
