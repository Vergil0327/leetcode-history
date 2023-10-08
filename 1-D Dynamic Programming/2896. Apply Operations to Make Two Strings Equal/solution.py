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
