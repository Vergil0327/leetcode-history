class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k

        nums.sort(reverse=True)
        if nums[0] > target: return False
        bitmask = 0 # record used nums[i] where i is bit position

        memo = {}
        
        def dfs(state, visited, cnt, start):
            if cnt == k: return True
            if state == target:
                canPartition = dfs(0, visited, cnt+1, 0)
                memo[visited] = canPartition
                return canPartition

            if visited in memo: return memo[visited]

            for i in range(start, len(nums)):
                if 1<<i & visited: continue
                if nums[i]+state>target: continue

                visited |= 1<<i
                if dfs(state+nums[i], visited, cnt, i+1): return True
                visited ^= 1<<i
                
            return False
        return dfs(0, bitmask, 0, 0)

# python TLE
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k

        nums.sort(reverse=True)
        if nums[0] > target: return False
        visited = [False] * len(nums)
        
        def dfs(state, visited, cnt, start):
            if cnt == k: return True
            if state == target:
                return dfs(0, visited, cnt+1, 0)

            for i in range(start, len(nums)):
                if visited[i]: continue
                if state+nums[i]>target: continue
                
                visited[i] = True
                if dfs(state+nums[i], visited, cnt, i+1): return True
                visited[i] = False
            return False
        return dfs(0, visited, 0, 0)