class Solution:
  def numberOfWays(self, num_people: int) -> int:
      mod = 10**9 + 7

      dp = [0] * (num_people+1)
      dp[0] = dp[2] = 1

      for i in range(4, num_people+1, 2):
          for j in range(0, i-1):
             dp[i] += dp[j] * dp[i-j-2]
             dp[i] %= mod
      return dp[num_people]
