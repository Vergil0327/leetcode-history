class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:

        res = -inf
        presum_r = presum_l = deletion_sum = 0
        _sum = Counter()

        for x in nums:
            presum_r += x

            res = max(res, presum_r - deletion_sum)

            _sum[x] = min(_sum[x], presum_l) + x # 這邊注意順序, 不能讓presum_l先被更新
            presum_l = min(presum_l, presum_r)

            deletion_sum = min(deletion_sum, presum_l, _sum[x])
        return res
