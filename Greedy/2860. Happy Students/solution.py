class Solution:
    def countWays(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        # check if we can pick none of nums
        res = 1 if nums[0] > 0 else 0
        
        for i in range(n):
            cnt = i+1
            if cnt > nums[i] and (i+1 == n or cnt < nums[i+1]):
                res += 1

        return res
