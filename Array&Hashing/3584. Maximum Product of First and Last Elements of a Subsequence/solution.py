class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)

        suffix_max=deque([-inf])
        suffix_min=deque([inf])
        for i in range(n-1, -1, -1):
            suffix_max.appendleft(max(nums[i], suffix_max[0]))
            suffix_min.appendleft(min(nums[i], suffix_min[0]))

        res = -inf
        for i in range(n-m+1):
            res = max(res, nums[i] * suffix_max[i+m-1])
            res = max(res, nums[i] * suffix_min[i+m-1])
        return res
    

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        if m == 1:
            return max(x * x for x in nums)

        res = -inf
        max_pref = nums[0]
        min_pref = nums[0]

        for j in range(m - 1, n):
            res = max(res,
                      max_pref * nums[j],
                      min_pref * nums[j])

            idx = j - (m - 1) + 1
            if idx < n:
                max_pref = max(max_pref, nums[idx])
                min_pref = min(min_pref, nums[idx])

        return res
        