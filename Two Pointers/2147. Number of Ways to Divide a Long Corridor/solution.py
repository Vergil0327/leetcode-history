class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7

        # remove leading plants and trailing plants
        n = len(corridor)
        i, j = 0, n-1
        while i < n and corridor[i] == "P":
            i += 1
        while j > i and corridor[j] == "P":
            j -= 1

        corridor = corridor[i:j+1]

        res = 1
        n = len(corridor)
        i = seats = 0
        totalSeats = 0
        while i < n:
            if corridor[i] == "S":
                seats += 1
                totalSeats += 1
            if seats == 2:
                
                j = i+1
                while j < n and corridor[j] == "P":
                    j += 1
                res *= j-i
                res %= mod
                
                seats = 0
                i = j-1
            i += 1

        return res if totalSeats > 0 and totalSeats%2==0 else 0
