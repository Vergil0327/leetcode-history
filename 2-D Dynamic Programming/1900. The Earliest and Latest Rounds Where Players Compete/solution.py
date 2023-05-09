class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        dpMin = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
        dpMax = [[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)]

        def dfs(n, A, B):
            if A + B == n+1: # symmetric
                return (1,1)

            if dpMin[n][A][B] != 0:
                return (dpMin[n][A][B], dpMax[n][A][B])

            if A > B:
                return dfs(n, B, A)
            
            if (A+B)/2 > (n+1)/2:
                return dfs(n, n+1-B, n+1-A)

            # Case 1
            # XXXXX A XXX B' XX MID XX B XXX A' XXXXX
            # _____   ___    _________
            #   x      y         z
            Bprime = n+1-B
            z = ((B-Bprime-1)+1)//2
            minRounds, maxRounds = n, 0
            if B > (n+1)//2:
                for x in range(A):
                    for y in range(Bprime-A):
                        rounds = dfs((n+1)//2, x+1, x+1+y+z+1)
                        minRounds = min(minRounds, rounds[0] + 1)
                        maxRounds = max(maxRounds, rounds[1] + 1)
            else:
                # Case 1
                # XXXXX A XXX B XX MID XX B' XXX A' XXXXX
                # _____   ___
                #   x      y
                for x in range(A):
                    for y in range(B-A):
                        rounds = dfs((n+1)//2, x+1, x+1+y+1)
                        minRounds = min(minRounds, rounds[0] + 1)
                        maxRounds = max(maxRounds, rounds[1] + 1)
            dpMin[n][A][B] = minRounds
            dpMax[n][A][B] = maxRounds
            return (minRounds, maxRounds)
        return dfs(n, firstPlayer, secondPlayer)