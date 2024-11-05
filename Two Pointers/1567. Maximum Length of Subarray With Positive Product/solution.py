class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        res = length = 0
        product = 1
        l = -1 # leftmost valid index of negative nums[i]
        for r in range(n):
            if l == -1 and nums[r] < 0:
                l = r

            if nums[r] == 0: # reset & try updating res
                if product > 0:
                    res = max(res, length)
                length = 0
                product = 1
                l = -1
            else:
                product *= nums[r]
                length += 1
                if product > 0:
                    res = max(res, length)
                else: # product < 0 => remove leftmost negative nums[i]
                    res = max(res, r-l)
        return res
