# no need to memorize
class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        def dfs(start, length):
            if length % 2 != 0:
                ones = s.count('1', start, start + length)
                cost = flatCost if ones == 0 else length * ones * encCost
                return cost, ones
            
            half = length // 2
            left_cost, left_ones = dfs(start, half)
            right_cost, right_ones = dfs(start + half, half)
            
            ones = left_ones + right_ones
            base_cost = flatCost if ones == 0 else length * ones * encCost
            
            return min(base_cost, left_cost + right_cost), ones
            
        return dfs(0, len(s))[0]