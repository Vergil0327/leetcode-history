# O(n^2)
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp, maxScore = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
        for i in range(n):
            maxScore[i][i] = stoneValue[i]
        
        for j in range(1, n):
            mid, total, rightHalf = j, stoneValue[j], 0
            for i in range(j - 1, -1, -1):
                total += stoneValue[i]
                while (rightHalf + stoneValue[mid]) * 2 <= total:
                    rightHalf += stoneValue[mid]
                    mid -= 1
                dp[i][j] = maxScore[i][mid] if rightHalf * 2 == total else (0 if mid == i else maxScore[i][mid - 1])
                dp[i][j] = max(dp[i][j], 0 if mid == j else maxScore[j][mid + 1])
                maxScore[i][j] = max(maxScore[i][j - 1], dp[i][j] + total)
                maxScore[j][i] = max(maxScore[j][i + 1], dp[i][j] + total)
        return dp[0][n - 1]

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = [0] + list(accumulate(stoneValue))

        @lru_cache(None)
        def dp(l, r):
            if r - l == 1: return 0
            if r - l == 2: return min(stoneValue[l], stoneValue[l+1])
            res = 0
            mid_left = bisect_right(prefix, (prefix[l] + prefix[r-1])//2) -1
            mid_right = bisect_right(prefix, (prefix[l+1] + prefix[r])//2)

            for m in range(
                max(l+1, mid_left),
                min(r, mid_right+1)
            ):
                left = prefix[m] - prefix[l]
                right = prefix[r] - prefix[m]
                
                if left <= right:
                    res = max(res, left + dp(l, m))
                
                if right <= left:
                    res = max(res, right + dp(m, r))

            return res

        return dp(0, len(stoneValue))


#####################################################
# Leetcode add new test cases, Top-Down will get TLE
#####################################################
# Bottom-Up
class Solution:
    def stoneGameV(self, values: List[int]) -> int:
        n = len(values)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + values[i-1]
        
        # dp[i][j]: the maximum score we can get between values[i:j]
        dp = [[0] * (n+1) for _ in range(n+1)]

        # base case: choose minimum one between two values
        for i in range(n-1):
            dp[i][i+1] = min(values[i], values[i+1])

        for length in range(3, n+1):
            for i in range(0, n-length+1): # j = i+length-1 < n
                j = i+length-1

                for mid in range(i+1, j+1):
                    left = presum[mid] - presum[i] # sum(values[i:mid])
                    right = presum[j+1] - presum[mid] # sum(values[mid:j+1])

                    if left < right:
                        dp[i][j] = max(dp[i][j], left + dp[i][mid-1])
                    elif left > right:
                        dp[i][j] = max(dp[i][j], right + dp[mid][j])
                    else:
                        dp[i][j] = max(dp[i][j], left + max(dp[i][mid-1], dp[mid][j]))

        return dp[0][n-1]

# Top-Down: O(n^3)
class Solution:
    def stoneGameV(self, values: List[int]) -> int:
        n = len(values)
        if n == 1: return 0

        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + values[i-1]

        @lru_cache(None)
        def dfs(l, r):
            if r==l: return 0
            
            scores = -inf
            for mid in range(l+1, r+1):
                left = presum[mid]-presum[l] # sum(values[l:mid])
                right = presum[r+1]-presum[mid] # sum(values[mid:r+1])
                
                if left < right:
                    scores = max(scores, dfs(l, mid-1) + left)
                elif left > right:
                    scores = max(scores, dfs(mid, r) + right)
                else:
                    scores = max(scores, dfs(l, mid-1) + left, dfs(mid, r) + right)
            return scores
        return dfs(0, len(values)-1)

# Top-Down - straightforward O(n^4)
class Solution:
    def stoneGameV(self, values: List[int]) -> int:
        n = len(values)
        if n == 1: return 0

        @lru_cache(None)
        def dfs(values):
            if len(values) == 1: return 0
            
            scores = -inf
            for mid in range(1, len(values)):
                left = sum(values[:mid])
                right = sum(values[mid:])
                
                if left < right:
                    scores = max(scores, dfs(tuple(values[:mid])) + left)
                elif left > right:
                    scores = max(scores, dfs(tuple(values[mid:])) + right)
                else:
                    scores = max(scores, dfs(tuple(values[:mid])) + left, dfs(tuple(values[mid:])) + right)
            return scores
        return dfs(tuple(values))