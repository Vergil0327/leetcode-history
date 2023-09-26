from sortedcontainers import SortedList
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        nums.sort()
        res = nums[n-1]-nums[0]
        # left = nums[0:i]
        # right = nums[i+1:n-1]
        for i in range(n-1):
            mx = max(nums[i]+k, nums[n-1]-k)
            mn = min(nums[0]+k, nums[i+1]-k)
            res = min(res, mx-mn)
        return res
