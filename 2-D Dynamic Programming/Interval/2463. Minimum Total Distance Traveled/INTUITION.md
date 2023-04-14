# Intuition

first of all, factory[j] should fix some robots near itself,
so it's intuitively to sort robot and factory by position first.

then we use DFS to explore factory[j]

- factory[j] can try to pick robot[i] to fix if it still has enough capacity
  - `res = min(res, dfs(i+1, j, cap+1) + abs(factory[j][0] - robot[i]))`
- factory[j] can pass robot[i] and we can choose factory[j+1] to fix robot[i]
  - `res = dfs(i, j+1, 0)`

**base case**

if we fix all of the robots which means **i == m**, then we return distance `0`
if we can't fix all of the robots until j == n, it's invalid. let's return `inf`

```py
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        m, n = len(robot), len(factory)
        robot.sort()
        factory.sort()

        @lru_cache(None)
        def dfs(i, j, cap):
            if i == m: return 0
            if j == n: return inf
            
            # factory[j] don't fix robot[i]
            res = dfs(i, j+1, 0)

            # factory[j] fix robot[i]
            if cap < factory[j][1]:
                res = min(res, dfs(i+1, j, cap+1) + abs(factory[j][0] - robot[i]))
            return res

        return dfs(0, 0, 0)
```