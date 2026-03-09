class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prod = 1
        leftsum = sum(nums)
        res = n
        for i in range(n-1, -1, -1):
            leftsum -= nums[i]

            if leftsum == prod:
                res = i

            prod *= nums[i]

            if prod > leftsum: break
        return res if res < n else -1
