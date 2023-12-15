class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        beautiful = [1]
        while len(beautiful) < n:
            odd = [num*2-1 for num in beautiful]
            even = [num*2 for num in beautiful]
            beautiful = odd + even
        return [num for num in beautiful if num <= n]

class Solution:
    def beautifulArray(self, N):
        @lru_cache(None)
        def dfs(N):
            if N == 1: return (1,)
            odd = dfs((N+1)//2)
            even = dfs(N//2)
            return [i*2-1 for i in odd] + [i*2 for i in even]
        
        return dfs(N)