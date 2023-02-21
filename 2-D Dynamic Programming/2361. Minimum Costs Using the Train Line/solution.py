class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)

        # dpReg[i] the minimum cost to reach stop[i] from stop 0 ended with regular route. (1-indexed)
        # dpExp[i] the minimum cost to reach stop[i] from stop 0 ended with express route. (1-indexed)
        dpReg = [inf] * (n+1)
        dpExp = [inf] * (n+1)
        
        # base case
        dpReg[0] = 0
        dpExp[0] = expressCost # !!! important, initial cost is expressCost

        # append first stop then we can start from i = 1 to calculate the cost
        regular = [0] + regular
        express = [0] + express

        res = []
        for i in range(1, n+1):
            dpReg[i] = min(dpReg[i-1] + regular[i], dpExp[i-1] + regular[i])
            dpExp[i] = min(dpReg[i-1] + expressCost + express[i], dpExp[i-1] + express[i])
            res.append(min(dpReg[i] + dpExp[i]))
        return res
