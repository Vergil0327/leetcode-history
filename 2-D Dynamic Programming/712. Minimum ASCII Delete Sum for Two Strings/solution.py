# explanation: https://www.youtube.com/watch?v=YPRHj16y6N4
"""
definition:
    dp[i][j]: lowest ASCII sum of deleted characters from s1[i:] and s2[j:]

base case:
    dp[0][0]: s1[:0] = "", s2[:0] = "" by definition
        therefore, lowest ADCII sum = dp[0][0] = 0

    dp[0][j]: s1[:0]= "", s2[:j] = "YYYYYYYY"
        -> we need to delete entire s2[:j] to make s1[:i] match s2[:j]
        -> dp[0][j] = dp[0][j-1] + ord(s2[j])

    dp[i][0]: s1[:0]= "XXXXXXXXX", s2[:j] = ""
        -> we need to delete entire s1[:i] to make s1[:i] match s2[:j]
        -> dp[i][0] = dp[i-1][0] + ord(s1[i])

state transfer:
    1. s1[i] == s2[j], then we don't delete any character
    2. s1[i] != s2[j], we have 2 choices to find minimum ASCII sum.
        i. delete s1[i], then continue comparing rest of them -> assume s2[j] can match afterwards.
            ex.
                s1[:i] = "AAAAAC" and s1[i+1] = B
                s2[:j] = "AAAAAB"
                -> s2[j] = "B" can match s1[i+1]
        ii. delete s2[j], then continue comparing rest of them -> assume s1[i] can match afterwards
"""
# time: O(mn)
# space: O(mn)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp[i][j]:  lowest ASCII sum of deleted characters from s1[i:] and s2[j:]
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        dp[0][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        
        return dp[m][n]

        # XXXX A
        # YYYYYY B
        # YYYYYY A

# time: O(mn)
# space: O(n)
# since our dp[i][j] only depends on previous state of dp
# we can cast 2-D array to 1-D array
class SolutionSpaceOptimized:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp[i][j]:  lowest ASCII sum of deleted characters from s1[i:] and s2[j:]
        m, n = len(s1), len(s2)
        # dp = [[0] * (n+1) for _ in range(m+1)]
        dp = [0] * (n+1)
        prevDp = [0] * (n+1)
        
        for j in range(1, n+1):
            # dp[0][j] = dp[0][j-1] + ord(s2[j-1])
            prevDp[j] = prevDp[j-1] + ord(s2[j-1])

        for i in range(1, m+1):
            # for i in range(1, m+1):
            #     dp[i][0] = dp[i-1][0] + ord(s1[i-1])
            dp[0] = prevDp[0]+ord(s1[i-1])
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[j] = prevDp[j-1]
                else:
                    dp[j] = min(prevDp[j] + ord(s1[i-1]), dp[j-1] + ord(s2[j-1]))
            dp, prevDp = prevDp, dp

        return prevDp[n]