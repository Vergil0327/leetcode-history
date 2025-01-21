class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        @cache
        def dfs(l, r, colorL, colorR):
            if l > r: return 0
            
            res = inf
            for color1 in range(3):
                if colorL == color1: continue
                for color2 in range(3):
                    if color1 == color2: continue
                    if colorR == color2: continue
                    res = min(res, dfs(l+1, r-1, color1, color2) + cost[l][color1] + cost[r][color2])
            return res

        return dfs(0, n-1, -1, -1)