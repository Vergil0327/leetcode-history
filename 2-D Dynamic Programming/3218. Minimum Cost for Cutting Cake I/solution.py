class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut = [0] + horizontalCut
        verticalCut = [0] + verticalCut

        @cache
        def dfs(left, right, top, bottom):
            if left+1 == right and top+1 == bottom: return 0
            res = inf
            for i, cost in enumerate(horizontalCut):
                if top < i < bottom:
                    res = min(res, dfs(left, right, top, i) + dfs(left, right, i, bottom) + cost)
            for i, cost in enumerate(verticalCut):
                if left < i < right:
                    res = min(res, dfs(left, i, top, bottom) + dfs(i, right, top, bottom) + cost)
            return res  
            
        return dfs(0, n, 0, m)
