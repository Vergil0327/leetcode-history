class SolutionTopDown:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp[i][j]:  lowest ASCII sum of deleted characters from s1[i:] and s2[j:]
        m, n = len(s1), len(s2)
        
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m and j == n:
                return 0

            if i == m:
                return sum([ord(ch) for ch in s2[j:]]) 
            if j == n:
                return sum([ord(ch) for ch in s1[i:]])
            
            if s1[i] == s2[j]:
                asciiSum = dfs(i+1, j+1)
            else:
                asciiSum = min(dfs(i+1, j) + ord(s1[i]), dfs(i, j+1) + ord(s2[j]))
            return asciiSum
        
        return dfs(0, 0)

class SolutionTopDownPrefixSum:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp[i][j]:  lowest ASCII sum of deleted characters from s1[i:] and s2[j:]
        m, n = len(s1), len(s2)
        
        prefix1 = [0] * (m+1)
        for i in range(m-1, -1, -1):
            prefix1[i] = prefix1[i+1]+ord(s1[i])

        prefix2 = [0] * (n+1)
        for j in range(n-1, -1, -1):
            prefix2[j] = prefix2[j+1]+ord(s2[j])
        
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m and j == n:
                return 0

            if i == m:
                return prefix2[j]
            if j == n:
                return prefix1[i]
            
            if s1[i] == s2[j]:
                asciiSum = dfs(i+1, j+1)
            else:
                asciiSum = min(dfs(i+1, j) + ord(s1[i]), dfs(i, j+1) + ord(s2[j]))
            return asciiSum
        
        return dfs(0, 0)