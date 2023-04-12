class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == "0": return 0
        
        n = len(num)

        presum_dp = [[0]*(n+1) for _ in range(n)]

        for i in range(n):
            for length in range(1, (i+1)+1):
                j = i-length+1

                # leading zero
                if nums[j] == "0": continue
                
                ways = 0
                if length == i+1: # j = 0
                    ways = 1
                else:
                    length2 = min(length, j)
                    if num[j:i] < num[j-length:j]:
                        length2 -= 1

                    # leading zero
                    while length2 >= 1 and num[j-length2] == "0":
                        length2 -= 1
                    
                    if length2 > 0:
                        ways = presum_dp[j-1][length2]
                presum_dp[i][length] = presum_dp[i-1][length-1] + ways

        return presum_dp[n-1][n]

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == "0": return 0
        
        n = len(num)

        lcs = [[0] * (n+1) for _ in range(n+1)] # longest common substring
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if num[i] == num[j]:
                    lcs[i][j] = lcs[i+1][j+1] + 1

        presum_dp = [[0]*(n+1) for _ in range(n)]

        for i in range(n):
            for length in range(1, (i+1)+1):
                j = i-length+1

                # leading zero
                if num[j] == "0":
                    presum_dp[i][length] = presum_dp[i][length-1]
                    continue
                
                dp = 0
                if length == i+1: # j = 0
                    dp = 1
                else:
                    length2 = min(length, j)
                    
                    # if length2 == length and num[j:i+1] < num[j-length2:j]:
                    #     length2 -= 1
                    if length2 == length and lcs[j][j-length2] < length2 and num[j+lcs[j][j-length2]] < num[j-length2+lcs[j][j-length2]]:
                        length2 -= 1
                    
                    # leading zero
                    while length2 >= 1 and num[j-length2] == "0":
                        length2 -= 1
                    
                    if length2 > 0:
                        dp = presum_dp[j-1][length2]
                presum_dp[i][length] = (presum_dp[i][length-1] + dp) % 1_000_000_007

        return presum_dp[n-1][n]