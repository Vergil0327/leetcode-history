# Brute force
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
