# Top-Down + Memorization

# O(nk)
# we can do get partial maximum stepwisely to reduce O(n) to O(1)
# don't need to recalculate at every iteration
class OptimizedSolution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        @functools.lru_cache(None)
        def dfs(i):
            if i == n: return 0
            
            res = -float('inf')
            length = 0
            partialMax = -float("inf")
            for j in range(i, min(i+k, n)):
                length += 1
                partialMax = max(partialMax, arr[j]) # O(1)
                res = max(res, dfs(j+1) + partialMax * length)
            return res
        return dfs(0)

# Runtime: 8112 ms, faster than 5.17%
# O(nk * k), last k for max(arr[i:j+1])
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        @functools.lru_cache(None)
        def dfs(i):
            if i == n: return 0
            
            res = -float('inf')
            for j in range(i, min(i+k, n)): # O(k^2) because max(arr[i:j+1]) is O(k)
                res = max(res, dfs(j+1) + max(arr[i:j+1]) * (j-i+1))
            return res
        return dfs(0)