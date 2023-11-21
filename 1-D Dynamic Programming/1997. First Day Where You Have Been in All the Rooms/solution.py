class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        mod = 10**9 + 7

        n = len(nextVisit)
        dp = [0] * n
        for i in range(n-1):
            dp[i+1] = (dp[i] + 1 + dp[i]-dp[nextVisit[i]] + mod)%mod + 1 # 注意, 有減法, 小心因為減法 + 取餘造成負數
        
        return dp[n-1]%mod
