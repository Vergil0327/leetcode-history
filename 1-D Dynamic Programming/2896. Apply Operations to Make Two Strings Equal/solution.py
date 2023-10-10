class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        arr = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                arr.append(i)
        n = len(arr)
        if n%2 == 1: return -1
        if n == 0: return 0

        dp = [inf] * n
        dp[0] = x/2
        for i in range(1, n):
            dp[i] = dp[i-1] + x/2
            dp[i] = min(dp[i], (dp[i-2] if i-2 >= 0 else 0) + arr[i]-arr[i-1])
        return int(dp[n-1])

# O(n^3)
# 區間型dp
# dp[i][j]: the min operations for arr[i:j]
# dp[i][j] = min(dp[i][k] + dp[k+1][j])
# 同時對於將arr[i]跟arr[j]配對, 可以得到一個解是: dp[i][j] = dp[i+1][j-1] + min(x, arr[j]-arr[i])
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        arr = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                arr.append(i)
        n = len(arr)
        if n%2 == 1: return -1
        if n == 0: return 0

        dp = [[inf] * n for _ in range(n)]
        for i in range(n-1):
            dp[i][i+1] = min(x, arr[i+1]-arr[i])
        for length in range(4, n+1, 2):
            for i in range(0, n-length+1):
                j = i+length-1
                dp[i][j] = dp[i+1][j-1] + min(x, arr[j]-arr[i])
                for k in range(i+1, j-1, 2):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
        return dp[0][n-1]