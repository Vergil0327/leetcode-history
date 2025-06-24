class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        numWays = [1] + numWays

        res = []        
        for i in range(1, n+1):
            if numWays[i] == 0: continue

            if numWays[i] == 1:
                res.append(i)

                for j in range(n, i-1, -1):
                    numWays[j] -= numWays[j-i]
            else:
                return []

        return res