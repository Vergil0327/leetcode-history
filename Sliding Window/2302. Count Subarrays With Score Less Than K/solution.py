# [l:r), right exclusive
# fixed `r`, we got r-l valid `l` positions which means `r-l` valid subarrays
# [X X X X X X] X
#  l            r
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = 0
        res = total = count = 0
        while r < n:
            total += nums[r]
            count += 1
            r += 1

            while l < r and total*count >= k:
                total -= nums[l]
                count -= 1
                l += 1

            res += r-l
        return res
