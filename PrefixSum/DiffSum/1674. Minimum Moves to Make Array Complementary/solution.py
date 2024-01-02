class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        diff_steps = defaultdict(int)
        for i in range(n//2):
            x, y = nums[i], nums[n-1-i]
            
            diff_steps[2] += 2
            diff_steps[min(x,y)+1] -= 1
            diff_steps[x+y] -= 1
            diff_steps[x+y+1] += 1
            diff_steps[max(x,y)+limit+1] += 1

        res = n
        steps = 0
        for target_pair_sum in range(2, limit*2+1):
            steps += diff_steps[target_pair_sum]
            res = min(res, steps)
        return res

from sortedcontainers import SortedDict
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        diff_steps = SortedDict()
        for i in range(n//2):
            x, y = nums[i], nums[n-1-i]
            
            diff_steps[2] = diff_steps.get(2, 0) + 2
            diff_steps[min(x,y)+1] = diff_steps.get(min(x,y)+1, 0) - 1
            diff_steps[x+y] = diff_steps.get(x+y, 0) - 1
            diff_steps[x+y+1] = diff_steps.get(x+y+1, 0) + 1
            diff_steps[max(x,y)+limit+1] = diff_steps.get(max(x,y)+limit+1, 0) + 1

        res = n
        steps = 0
        for target_pair_sum in diff_steps:
            steps += diff_steps[target_pair_sum]
            res = min(res, steps)
        return res