# Top-Down DP
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def leftRotate(s):
            return s[1:] + s[:1]
        def rightRotate(s):
            return s[-1:] + s[:-1]
        
        @lru_cache(None)
        def dfs(i, ring):
            if i == len(key): return 0
            
            leftStep = 1 # pressing button
            s1 = ring
            while s1[0] != key[i]:
                s1 = leftRotate(s1)
                leftStep += 1
            steps1 = leftStep + dfs(i+1, s1)
            
            rightStep = 1 # pressing button
            s2 = ring
            while s2[0] != key[i]:
                s2 = rightRotate(s2)
                rightStep += 1
            steps2 = rightStep + dfs(i+1, s2)

            return min(steps1, steps2)
        return dfs(0, ring)
            
# Top-Down DP - Optimized
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        charAt = defaultdict(list)
        for i in range(len(ring)):
            charAt[ring[i]].append(i)
        
        n = len(ring)
        @lru_cache(None)
        def dfs(i, ringAt):
            if i == len(key): return 0
            
            minSteps = inf
            for j in charAt[key[i]]:
                delta = abs(j-ringAt)
                minRotate = min(delta, n-delta) # left rotate or right rotate
                steps = dfs(i+1, j) + 1 + minRotate # 1 for pressing button
                minSteps = min(minSteps, steps)
            return minSteps
        return dfs(0, 0)

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ringAt = defaultdict(list)
        for i in range(len(ring)):
            ringAt[ring[i]].append(i)
        
        R, K = len(ring), len(key)
        
        # dp[i][currRingAt] : minimum steps to spell for key[:i]
        dp = [[inf] * R for _ in range(K)]

        # base case
        for pos in ringAt[key[0]]:
            delta = pos-0
            dp[0][pos] = min(dp[0][pos], min(delta, R-delta))

        for i in range(1, K):
            for curr in ringAt[key[i]]:
                for prev in ringAt[key[i-1]]:
                    delta = abs(prev-curr)
                    dp[i][curr] = min(dp[i][curr], dp[i-1][prev] + min(delta, R-delta))
        
        res = inf
        for pos in ringAt[key[K-1]]:
            res = min(res, dp[K-1][pos])
        return res + K # K for K times of pressing button
