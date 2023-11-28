# Concise
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = [i for i,c in enumerate(corridor) if c == 'S']
        res = 1
        mod = 10**9+7
        for i in range(1,len(seats) - 1,2):
            res *= seats[i+1] - seats[i]
            res %= mod
        return res if len(seats) % 2 == 0 and len(seats) >= 2 else 0