# Brute Force
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        ROWS = len(mat)
        
        dp = {0} # dp hashset store all possible sum
        for i in range(ROWS):
            nxt = set()
            for _sum in dp:
                for v in mat[i]:
                    nxt.add(_sum+v)
            dp = nxt
        return min(abs(_sum-target) for _sum in dp)

# Optimization

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        ROWS = len(mat)
        
        dp = {0} # dp hashset store all possible sum
        for i in range(ROWS):
            nxt = set()
            greaterThanTarget = inf
            for _sum in dp:
                for v in mat[i]:
                    if _sum+v <= target:
                        nxt.add(_sum+v)
                    else:
                        greaterThanTarget = min(greaterThanTarget, _sum+v)
            if greaterThanTarget != inf:
                nxt.add(greaterThanTarget)
            dp = nxt
        return min(abs(_sum-target) for _sum in dp)