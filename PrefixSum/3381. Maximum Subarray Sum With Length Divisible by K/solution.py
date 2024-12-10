class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = list(accumulate(nums, initial=0))

        res = -inf
        seen = defaultdict(lambda: inf)
        for size in range(1, n + 1):
            if size % k == 0:
                res = max(res, presum[size])

            if (size % k) in seen:
                res = max(res, presum[size] - seen[size % k])

            seen[size % k] = min(seen[size % k], presum[size])
        return res
