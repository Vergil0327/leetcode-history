class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        splits = []
        for i in range(n-1):
            splits.append(weights[i]+weights[i+1])
        splits.sort()
        
        # max k-1 cuts - min k-1 cuts
        k -= 1
        return sum(splits[len(splits)-k:]) - sum(splits[:k])

# Brute Force - TLE
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        
        @lru_cache(None)
        def dfs(i, k):
            if i == n:
                if k == 0: return 0, 0
                return inf, -inf
            
            MIN, MAX = inf, -inf
            for j in range(i, n):
                costMin, costMax = dfs(j+1, k-1)
                if costMin == inf: continue
                if costMax == -inf: continue
                costMin += weights[i] + weights[j]
                costMax += weights[i] + weights[j]
                MIN = min(MIN, costMin)
                MAX = max(MAX, costMax)
            
            return (MIN, MAX)
            
        MIN, MAX = dfs(0, k)
        return MAX-MIN