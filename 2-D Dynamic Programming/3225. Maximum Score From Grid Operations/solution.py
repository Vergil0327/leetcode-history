# TLE version
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_presum = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        @cache
        def dfs(col: int, preHei: int, prePreHei: int) -> int:
            if col >= n: return 0

            res = 0
            for h in range(n + 1):
                if preHei >= h:
                    curScoreFromLeft = col_presum[col][preHei] - col_presum[col][h]
                    res = max(res, dfs(col + 1, h, preHei) + curScoreFromLeft)
                elif prePreHei > preHei:  # preHei already < h and also preHei < prePreHei => 凹形 => already calculated above at previous round
                    res = max(res, dfs(col + 1, h, preHei))
                else:  # 此時h > preHei, 代表高度遞增 => 對於col-1來說, 必須補上col高出col-1那段高度差的得分
                    prevScoreFromRight = col_presum[col - 1][h] - col_presum[col - 1][preHei]
                    res = max(res, dfs(col + 1, h, preHei) + prevScoreFromRight)
            return res

        return max(dfs(1, h, 0) for h in range(n + 1))

# Optimized version
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_presum = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        @cache
        def dfs(col: int, preHei: int, isPreHeiDec: bool) -> int:
            if col >= n: return 0

            res = 0
            for h in range(n + 1):
                if preHei == h:
                    res = max(res, dfs(col + 1, h, False))
                if preHei > h:
                    curScoreFromLeft = col_presum[col][preHei] - col_presum[col][h]
                    res = max(res, dfs(col + 1, h, True) + curScoreFromLeft)
                elif isPreHeiDec:  # preHei already < h and also preHei < prePreHei => 凹形 => already calculated above at previous round
                    res = max(res, dfs(col + 1, h, False))
                else:  # 此時h > preHei, 代表高度遞增 => 對於col-1來說, 必須補上col高出col-1那段高度差的得分
                    prevScoreFromRight = col_presum[col - 1][h] - col_presum[col - 1][preHei]
                    res = max(res, dfs(col + 1, h, False) + prevScoreFromRight)
            return res


        return max(dfs(1, h, False) for h in range(n + 1))