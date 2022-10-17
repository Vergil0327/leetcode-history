class Solution(object):
    def canCross(self, stones):
        n=len(stones)
        dp={0:{0}}
        for i in range(1,n):
            dp[stones[i]]=set()
            
        for i in range(n):
            for unit in dp[stones[i]]:
                for k in {unit-1,unit,unit+1}:
                    if stones[i]+k in dp and k>0:
                        dp[stones[i]+k].add(k)
        return dp[stones[-1]]

class SolutionTopDown(object):
    def canCross(self, stones):
        stoneSet = set(stones)
        visited = set()
        
        def dfs(value,unit):
            if (value+unit not in stoneSet) or ((value,unit) in visited):
                return False
            if value+unit == stones[-1]:
                return True
            visited.add((value,unit))
            return dfs(value+unit,unit) or dfs(value+unit,unit-1) or dfs(value+unit,unit+1)
        return dfs(stones[0],1)

class SolutionSlow(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False
        
        memo = {}
        def dfs(i, unit):
            if i == len(stones)-1:
                return True
            
            if i >= len(stones):
                memo[(i, unit)] = False
                return False
            
            if (i, unit) in memo:
                return memo[(i, unit)]
            
            for j in range(i+1, len(stones)):
                if stones[j] == stones[i]+unit-1:
                    if dfs(j, unit-1):
                        return True
                if stones[j] == stones[i]+unit:
                    if dfs(j, unit):
                        return True
                if stones[j] == stones[i]+unit+1:
                    if dfs(j, unit+1):
                        return True
                    
            memo[(i, unit)] = False
            return False    
            
            
        return dfs(1, 1)
        