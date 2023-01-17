### Concise
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)

        prefix1 = [0] * (n+1)
        for i in range(1, n+1):
            prefix1[i] = prefix1[i-1] + (1 if s[i-1] == "1" else 0)
        
        suffix0 = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix0[i] = suffix0[i+1] + (1 if s[i] == "0" else 0)

        flips = inf
        flips = min(flips, suffix0[0]) # all 0 case
        flips = min(flips, prefix1[n]) # all 1 case
        # zeros followed by ones case
        for i in range(n):
            flips = min(flips, prefix1[i] + suffix0[i])

        return flips
