# https://leetcode.com/problems/minimum-total-distance-traveled/discuss/2783305/Python-DP-Solution
# Top-Down DFS with memorization
# strategy: take or not take
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        # j-th factory with current limit fix i-th robot
        # if j-th factory reach limit, use next factory to fix i-th robot
        @functools.lru_cache(None)
        def dfs(i, j, limit):
            if i == len(robot):
                return 0
            
            if j >= len(factory):
                return float("inf")
            
            dist1 = dfs(i, j+1, 0)
            dist2 = dfs(i+1, j, limit+1) + abs(robot[i]-factory[j][0]) if limit < factory[j][1] else float("inf")
            
            return min(dist1, dist2)
        
        return dfs(0, 0, 0)


# https://leetcode.com/problems/minimum-total-distance-traveled/discuss/2783305/Python-DP-Solution
class SolutionBottomUp:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        dp = [float("inf")]* (len(robot)+1)
        dp[len(robot)] = 0
        for j in range(len(factory)-1, -1, -1):
            for i in range(len(robot)):
                curr = 0
                
                limit = min(factory[j][1], len(robot)-i)
                for k in range(1, limit+1):
                    curr += abs(robot[i+k-1]-factory[j][0])
                    dp[i] = min(dp[i], dp[i+k] + curr)
        return dp[0]