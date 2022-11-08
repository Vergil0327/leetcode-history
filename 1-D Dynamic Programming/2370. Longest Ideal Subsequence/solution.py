"""
DP definition: dp[i] longest length of ideal subsequence s[:i]
and we get state transfer eq.:

dp[i] = max(dp[i], dp[j]+1) for every abs(ord(s[i])-ord(s[j])) <= k

we also maintain an array closest to store index of X character
    - X is last character of longest ideal subsequence ending at j-th position.
    - X is from a to z

ex.
"kpaaaaavkccccji", k=4, ans:2
 j'      j    i  => consider s[i], append after j position is longer than appending after j'
 j = closest["k"]
"""
# explanation: https://www.youtube.com/watch?v=NlwpGpH4nLA&ab_channel=HuifengGuan
# O(26n)
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        OFFSET = ord("a")

        dp = [1] * N
        closest = [-1] * 26 # index of a-z closest to s[i]
        longest = 1
        for i in range(0, N):
            shift = ord(s[i])-OFFSET
            for alphabet in range(max(0, shift-k), min(26, shift+k+1)):
                j = closest[alphabet]
                if j != -1:
                    dp[i] = max(dp[i], dp[j]+1)
            closest[ord(s[i])-OFFSET] = i
            longest = max(longest, dp[i])

        return longest

    # Top-Dwon TLE
    def longestIdealStringTLE(self, s: str, k: int) -> int:
        N = len(s)
        OFFSET = ord("a")

        def dfs(i, prevCh, memo):
            if i == N: return 0

            if (i, prevCh) in memo:
                return memo[(i, prevCh)]
            
            if abs(ord(s[i])-OFFSET-prevCh) <=k or prevCh == -1:
                memo[(i, prevCh)] = max(dfs(i+1, prevCh, memo), 1 + dfs(i+1, ord(s[i])-OFFSET, memo))
            else:
                memo[(i, prevCh)] = dfs(i+1, prevCh, memo)
            return memo[(i, prevCh)]
        return dfs(0, -1, {})

"""
since subsequence don't need to be consecutive,
we can think dynamic programming on character

keep appending current s[i] to [s[i]-k, s[i]+k],
the maximum should be answer
"""
class BestSolution:
    # Bottom-Up
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for ch in s:
            num = ord(ch)-ord("a")
            l = max(0, num-k)
            r = min(25, num+k)
            dp[num] = max(dp[l:r+1])+1
        return max(dp)

    # Top-Down
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        OFFSET = ord("a")

        def dfs(i):
            if i == -1: return [0] * 26
            
            seq = dfs(i-1)

            num = ord(s[i])-OFFSET
            lo = max(0, ord(s[i])-OFFSET-k)
            hi = min(26, ord(s[i])-OFFSET+k+1)
            seq[num] = max(seq[lo:hi])+1
            return seq
        return max(dfs(N-1))

class SolutionBruteForce:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)

        dp = [1] * N
        for i in range(0, N):
            for j in range(0, i):
                if abs(ord(s[i])-ord(s[j])) <= k:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)