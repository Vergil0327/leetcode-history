# DFS
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        
        @lru_cache(None)
        def dfs(i):
            if i >= n or i < 0: return False
            if arr[i] == 0: return True

            if i in visited: return False
            visited.add(i)

            if dfs(i+arr[i]): return True
            if dfs(i-arr[i]): return True
            return False
        
        return dfs(start)