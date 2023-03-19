class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.res = 0
        def dfs(state, i):
            if i == n:
                if not state: return
                self.res += 1
                return
            if i > n:
                return
            
            dfs(state, i+1)
            if nums[i]+k not in state and nums[i]-k not in state:
                state[nums[i]] += 1
                dfs(state, i+1)
                state[nums[i]] -= 1
                if state[nums[i]] == 0:
                    del state[nums[i]]
            
        dfs(defaultdict(int), 0)
        return self.res