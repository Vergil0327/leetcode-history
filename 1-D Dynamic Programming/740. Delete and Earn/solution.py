
# Top-Down + Memorization: O(n)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        nums.sort()

        @functools.lru_cache(None)
        def dfs(i):
            if i == n: return 0
            
            # pick
            points = dfs(i+1)
            
            # skip
            nextIdx = i+1
            while nextIdx < n and (nums[nextIdx] == nums[i] or nums[nextIdx] == nums[i]+1):
                nextIdx += 1

            points = max(points, dfs(nextIdx) + counter[nums[i]] * nums[i])
            return points
        return dfs(0)

# Botton-Up: O(n)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums.sort()
        maxVal = nums[-1]
        
        # house robber problem in value domain
        # pick[i]: maximum number of points by picking i
        # skip[i]: maximum number of points by skipping i
        pick, skip = [0]*(maxVal+1), [0]*(maxVal+1)
        for i in range(1, maxVal+1): # 1 <= nums[i] <= sorted(nums)[-1]
            pick[i] = skip[i-1] + counter[i] * i # take i all at once
            skip[i] = max(skip[i-1], pick[i-1])
        
        return max(pick[-1], skip[-1])
