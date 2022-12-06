# straight-forward
# count frequency of each num, then backtracking
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        counter = Counter(nums)

        def dfs(state):
            nonlocal counter
            if len(state) == n:
                res.append(state.copy())
                return

            for num in counter:
                if counter[num] == 0: continue
                state.append(num)
                counter[num] -= 1
                dfs(state)
                counter[num] += 1
                state.pop()
        dfs([])
        return res

# https://www.youtube.com/watch?v=Vn2v6ajA7U0
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # we need to skip dupliate
        nums.sort()
        visited = 0 # using bitmask
        def dfs(state):
            nonlocal visited
            if len(state) == n:
                res.append(state.copy())
                return

            for j in range(n):
                if visited & 1<<j: continue
                if j > 0 and nums[j] == nums[j-1] and (visited & (1<<(j-1))) == 0: continue
                
                visited |= 1<<j
                state.append(nums[j])
                dfs(state)
                state.pop()
                visited ^= 1<<j
        dfs([])
        return res