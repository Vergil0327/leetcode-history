class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(state):
            if len(state) == len(nums):
                res.append(state.copy())
                return

            for num in nums:
                if num in visited: continue
                state.append(num)
                visited.add(num)
                dfs(state)
                state.pop()
                visited.remove(num)
        dfs([])
        return res


class SmartSolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(state, nums):
            if not nums:
                res.append(state.copy())
                return
            
            for i, num in enumerate(nums):
                dfs(state+[num], nums[:i] + nums[i+1:])
        dfs([], nums)
        return res

# Bitmask
# since nums.length <= 6, we can use 6 bit bitmast to replace `visited` hashset
# it's even more efficient than using array as `visited`
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def dfs(state, bitmask):
            if len(state) == len(nums):
                res.append(state.copy())
                return

            for i, num in enumerate(nums):
                if 1<<i & bitmask: continue
                state.append(num)
                bitmask |= 1<<i
                dfs(state, bitmask)
                state.pop()
                bitmask ^= 1<<i
        dfs([], 0)
        return res