class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = int(1e9+7)
        def isPrime(num):
            return num == "2" or num == "3" or num == "5" or num == "7"
        n = len(s)
        
        if not isPrime(s[0]): return 0
        if isPrime(s[-1]): return 0
        
        @functools.lru_cache(None)
        def dfs(i, k):
            if i == n-1 and k == 1:
                return 1
            if i >= n-1 or k == 0:
                return 0

            res = dfs(i+1, k) # skip current partition position
            if not isPrime(s[i]) and isPrime(s[i+1]): # valid partition, found valid ending position
                res += dfs(i+minLength, k-1) # since minLength at least, start finding next partition at i+minLength
            return res % MOD

        # must minlength-1 since what we check in dfs if ending position
        # if index 0 is valid starting point, our ending must be minLength-1 at least
        return dfs(minLength-1, k)
    
# 2023/04/13
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = set(["2","3","5","7"])
        if s[0] not in primes or s[-1] in primes: return 0

        validStart = [0]
        
        n = len(s)
        for i in range(n):
            if i+1 < n and s[i] not in primes and s[i+1] in primes:
                validStart.append(i+1)

        m = len(validStart)
        
        @lru_cache(None)
        def dfs(i, k):
            if k == 1: return 1
            if i >= m: return 0

            # skip i-th
            res = dfs(i+1, k) % 1_000_000_007

            # take i-th
            if n-validStart[i] >= minLength:
                # skip invalid start position
                j = i+1
                while j < m and validStart[j]-validStart[i] < minLength:
                    j += 1
                res = (res + dfs(j, k-1)) % 1_000_000_007
            
            return res
            
        # skip invalid start position
        i = 1
        while i < m and validStart[i] - validStart[0] < minLength:
            i += 1
        return dfs(i, k)

# Top-Down FAILED
class SolutionTLE:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = int(1e9+7)
        def isPrime(num):
            return num == "2" or num == "3" or num == "5" or num == "7"
        n = len(s)
        
        if not isPrime(s[0]): return 0
        if isPrime(s[-1]): return 0
        
        # index of valid starting character
        idxs = [0]
        for i in range(n-1):
            if not isPrime(s[i]) and isPrime(s[i+1]):
                idxs.append(i+1)

        @functools.lru_cache(None)
        def dfs(i, k):
            if k == 1:
                return 1 if n - idxs[i] >= minLength else 0

            res = 0
            for j in range(i+1, len(idxs)):
                if idxs[j]-idxs[i] >= minLength:
                    res += dfs(j, k-1)
            return res % MOD
        return dfs(0,k)

class SolutionTLE:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = int(1e9+7)
        def isPrime(num):
            return num == "2" or num == "3" or num == "5" or num == "7"
        n = len(s)
        
        @functools.lru_cache(None)
        def dfs(i, k):
            if i == n and k == 0:
                return 1
            if i == n or k == 0:
                return 0
            
            if not isPrime(s[i]): return 0

            res = 0
            for j in range(i+minLength, n+1):
                if not isPrime(s[j-1]):
                    if j-i < minLength: continue
                    res += dfs(j, k-1) % MOD

            return res % MOD
        return dfs(0,k)
