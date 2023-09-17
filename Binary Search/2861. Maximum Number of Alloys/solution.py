class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def check(i, mid):
            need = 0
            for j in range(n):
                need += max(0, composition[i][j]*mid - stock[j]) * cost[j]
            return need <= budget
        
        res = 0
        for i in range(k):
            l = r = 0
            for j in range(n):
                r = max(r, (budget+stock[j]*cost[j])//cost[j]+1)
            
            while l < r:
                mid = r - (r-l)//2
                if check(i, mid):
                    l = mid
                else:
                    r = mid-1
            res = max(res, l)
            
        return res
                