from bisect import bisect_left, bisect_right
from math import inf

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        arr = sorted(zip(robots, distance))
        n = len(arr)
        walls.sort()

        def count(l, r):
            if l > r:
                return 0
            return bisect_right(walls, r) - bisect_left(walls, l)

        dp = [[0,0] for _ in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = count(arr[0][0]-arr[0][1], arr[0][0]-1)

        for i in range(1, n+1):
            robot1, d1 = arr[i-1]
            robot2 = arr[i][0] if i < n else inf
            d2 = arr[i][1] if i < n else 0

            l1, r1 = robot1 + 1, min(robot1 + d1, robot2 - 1)
            l2, r2 = max(robot2 - d2, robot1 + 1), robot2 - 1
            
            left_bullet = count(l1, r1)
            right_bullet = count(l2, r2)
            overcount = count(max(l1, l2), min(r1, r2))

            dp[i][0] = max(dp[i-1][0] + left_bullet, dp[i-1][1])
            dp[i][1] = max(dp[i-1][0] + left_bullet + right_bullet - overcount, dp[i-1][1] + right_bullet)

        return max(dp[n]) + len(set(robots) & set(walls))