class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        total = OFFSET = sum(rods)

        dp = [[-inf] * (3*(total+1)) for _ in range(n+1)]
        dp[0][0+OFFSET] = 0

        rods = [0] + rods # shift to 1-indexed

        # dp[i][diff]: considering i-th round selection, the maximum height of left rod when difference is `diff`
        for i in range(1, n+1):
            for diff in range(-total, total+1):
                if dp[i-1][diff] == -inf: continue
                dp[i][diff+OFFSET] = max(dp[i][diff+OFFSET], dp[i-1][diff+OFFSET])                
                dp[i][diff+OFFSET+rods[i]] = max(dp[i][diff+OFFSET+rods[i]], dp[i-1][diff+OFFSET] + rods[i])
                dp[i][diff+OFFSET-rods[i]] = max(dp[i][diff+OFFSET-rods[i]], dp[i-1][diff+OFFSET])
            
        return dp[n][0+OFFSET] if dp[n][0+OFFSET] != -inf else 0

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        total = sum(rods)

        dp = [defaultdict(lambda: -inf) for _ in range(n+1)]
        dp[0][0] = 0

        rods = [0] + rods # shift to 1-indexed

        # dp[i][diff]: considering i-th round selection, the maximum height of left rod when difference is `diff`
        for i in range(1, n+1):
            for diff in range(-total, total+1):
                if dp[i-1][diff] == -inf: continue
                dp[i][diff] = max(dp[i][diff], dp[i-1][diff])
                dp[i][diff+rods[i]] = max(dp[i][diff+rods[i]], dp[i-1][diff] + rods[i])
                dp[i][diff-rods[i]] = max(dp[i][diff-rods[i]], dp[i-1][diff])
        return dp[n][0] if dp[n][0] != -inf else 0

# space-optimzed
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        total = sum(rods)

        dp = defaultdict(lambda: -inf)
        prevdp = defaultdict(lambda: -inf)
        prevdp[0] = 0

        rods = [0] + rods # shift to 1-indexed

        # dp[i][diff]: considering i-th round selection, the maximum height of left rod when difference is `diff`
        for i in range(1, n+1):
            for diff in range(-total, total+1):
                if prevdp[diff] == -inf: continue
                dp[diff] = max(dp[diff], prevdp[diff])
                dp[diff+rods[i]] = max(dp[diff+rods[i]], prevdp[diff] + rods[i])
                dp[diff-rods[i]] = max(dp[diff-rods[i]], prevdp[diff])
            dp, prevdp = prevdp, dp
        return prevdp[0] if prevdp[0] != -inf else 0

# time-optimized
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)

        dp = defaultdict(lambda: -inf)
        dp[0] = 0

        rods = [0] + rods # shift to 1-indexed

        # dp[i][diff]: considering i-th round selection, the maximum height of left rod when difference is `diff`
        for i in range(1, n+1):
            nxt = dp.copy()
            for diff in dp.keys():
                nxt[diff] = max(nxt[diff], dp[diff])
                nxt[diff+rods[i]] = max(nxt[diff+rods[i]], dp[diff] + rods[i])
                nxt[diff-rods[i]] = max(nxt[diff-rods[i]], dp[diff])
            dp = nxt
        return dp[0] if dp[0] != -inf else 0

"""
Intuition

find max sum of subset where sum(A) = sum(B)
    height {X X X X} {X X X X} X
               A         B
                               i
                               not pick
                               pick X in A
                               pick X in B
    
    considering first i element, if we can make 2 subsets be sumA and sumB
    dp[i][sumA][sumB] = true/false # dp[i][left_rod_height][right_rod_height]
    dp[i][sumA][sumB] = dp[i-1][sumA-rods[i]][sumB] or dp[i-1][sumA][sumB-rods[i]] or dp[i-1][sumA][sumB]
"""
class Solution_TLE:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        SUM = sum(rods)
        dp = [[[False] * (SUM+1) for _ in range(SUM+1)] for _ in range(n+1)]
        dp[0][0][0] = True

        rods = [0] + rods
        # sum(rods[i]) <= 5000
        for i in range(1, n+1):
            for sumA in range(SUM//2 + 1):
                for sumB in range(SUM//2 + 1):
                    dp[i][sumA][sumB] = dp[i][sumA][sumB] or dp[i-1][sumA][sumB]
                    if sumA-rods[i] >= 0:
                        dp[i][sumA][sumB] = dp[i][sumA][sumB] or dp[i-1][sumA-rods[i]][sumB]
                    if sumB-rods[i] >= 0:
                        dp[i][sumA][sumB] = dp[i][sumA][sumB] or dp[i-1][sumA][sumB-rods[i]]

        for s in range(SUM//2, -1, -1):
            if dp[n][s][s]: return s
        return 0