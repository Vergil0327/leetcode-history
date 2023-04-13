# O(N^3)
class SolutionTLE:
    def beautifulPartitions(self, s: str, K: int, minLength: int) -> int:
        n = len(s)
        MOD = int(1e9+7)
        
        def isprime(num):
            return num == "2" or num == "3" or num == "5" or num == "7"

        s = "#" + s # 1-index based

        # dp[i][k] : how many beautiful partitions if we split first i elements to k partition
        dp = [[0] * 1005 for _ in range(1005)] # constraints: 1 <= k, minLength <= s.length <= 1000
        dp[0][0] = 1 # 零字符組成零份 -> 1種方法

        for i in range(1, n+1): # end index
            for j in range(1, k+1):
                if isprime(s[i]):
                    dp[i][j] = 0 # can't be ending position
                    continue

                # start index, 前面j-1份所以k從j開始
                # k+minLength-1 <= i -> k <= i-minLength+1
                for k in range(j, (i-minLength+1)+1):
                    if isprime(s[k]):
                        dp[i][j] += dp[k-1][j-1] # be aware of edge case
                        dp[i][j] %= MOD
        return dp[n][K]


# XXXXX[XXXXX]
#       k   i
# dp[i][j] = dp[k-1][j-1]

class Solution:
    def beautifulPartitions(self, s: str, K: int, minLength: int) -> int:
        n = len(s)
        MOD = int(1e9+7)
        
        def isprime(num):
            return num == "2" or num == "3" or num == "5" or num == "7"

        s = "#" + s # 1-index based

        # dp[i][k] : how many beautiful partitions if we split first i elements to k partition
        dp = [[0] * 1005 for _ in range(1005)] # constraints: 1 <= k, minLength <= s.length <= 1000
        dp[0][0] = 1 # 零字符組成零份 -> 1種方法

        for j in range(1, K+1):
            presum = 0
            for i in range(1, n+1): # end index
                # if isprime(s[i]):
                #     dp[i][j] = 0 # can't be ending position
                #     continue

                # start index, 前面j-1份所以k從j開始
                # k+minLength-1 <= i -> K <= i-minLength+1
                # for k in range(j, (i-minLength+1)+1):
                #     if isprime(s[k]):
                #         dp[i][j] += dp[k-1][j-1] # be aware of edge case
                #         dp[i][j] %= MOD
                if i-minLength >= 0 and (not isprime(s[i-minLength])) and isprime(s[i-minLength+1]):
                    presum += dp[i-minLength][j-1]
                    presum %= MOD
                
                if not isprime(s[i]):
                    dp[i][j] = presum
                    dp[i][j] %= MOD
        return dp[n][K]


# XXXXX[XXXXX]
#       k   i
# dp[i][j] = dp[k-1][j-1]