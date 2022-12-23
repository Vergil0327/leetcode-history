# top-down DP (DFS + memorization)
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        memo = {}
        def dfs(i):
            count = 1 # including starting point

            if i in memo:
                return memo[i]

            for x in range(1, d+1):
                if i+x < n and arr[i+x] < arr[i]:
                    count = max(count, dfs(i+x)+1)
                else:
                    break

            for x in range(1, d+1):
                if i-x >= 0 and arr[i-x] < arr[i]:
                    count = max(count, dfs(i-x)+1)
                else:
                    break
            
            memo[i] = count
            return count
        
        jumps = 0
        for i, v in enumerate(arr):
            jumps = max(jumps, dfs(i))
        return jumps

# top-down DP (DFS + memorization) w/t visited
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        visited = set()

        memo = {}
        def dfs(i, visited):
            count = 1 # including starting point

            if i in memo:
                return memo[i]

            for x in range(1, d+1):
                if i+x < n and arr[i+x] < arr[i]:
                    if i+x not in visited:
                        visited.add(i+x)
                        count = max(count, dfs(i+x, visited)+1)
                        visited.remove(i+x)
                else: # must be monotonically decreasing
                    break

            for x in range(1, d+1):
                if i-x >= 0 and arr[i-x] < arr[i]:
                    if i-x not in visited:
                        visited.add(i-x)
                        count = max(count, dfs(i-x, visited)+1)
                        visited.remove(i-x)
                else: # must be monotonically decreasing
                    break
            
            memo[i] = count
            return count
        
        jumps = 0
        for i, _ in enumerate(arr):
            visited.add(i)
            jumps = max(jumps, dfs(i, visited))
            visited.remove(i)
        return jumps
