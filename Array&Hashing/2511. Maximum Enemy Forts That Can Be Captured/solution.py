# 2 pass - forward & backward
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        
        res = 0
        canMove = False
        curr = 0
        for i in range(1, n):
            if forts[i-1] == 1:
                canMove = True
                
            if canMove and forts[i] == 0:
                curr += 1
            else:
                if forts[i] == 1:
                    curr = 0
                    canMove = False
                if forts[i] == -1:
                    res = max(res, curr)
                    curr = 0
                    canMove = False
                    
        canMove = False
        curr = 0
        for i in range(n-2, -1, -1):
            if forts[i+1] == 1:
                canMove = True
                
            if canMove and forts[i] == 0:
                curr += 1
            else:
                if forts[i] == 1:
                    curr = 0
                    canMove = False
                if forts[i] == -1:
                    res = max(res, curr)
                    curr = 0
                    canMove = False
        
        return res

# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/solutions/2946493/python-attack-from-one-or-two-sides-explained/?orderBy=most_votes
class ConciseSolution:
    def captureForts(self, forts: List[int]) -> int:
        def attack(forts):
            MAX, curr = 0, -1
        
            for f in forts:
                if   f == 1 : curr = 0                       # start attack
                elif f == 0 : curr += curr >= 0              # count forts
                else        : curr, MAX = -1, max(curr,MAX)  # stop attack

            return MAX
        
        return max(attack(forts), attack(forts[::-1]))

# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/solutions/2946493/python-attack-from-one-or-two-sides-explained/?orderBy=most_votes
class OnePassSolution: 
    def captureForts(self, forts: List[int]) -> int:
        m = j = 0 
        for i, f in enumerate(forts): 
            if f != 0:
                if forts[j] == -f:
                    m = max(m, i-j-1)
                j = i 
        return m 