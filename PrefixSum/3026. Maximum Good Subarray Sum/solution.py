class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(lambda: inf)
        presum = 0
        res = -inf
        for i, num in enumerate(nums):
            presum += num
            if num-k in seen:
                res = max(res, presum-seen[num-k])
            if num+k in seen:
                res = max(res, presum-seen[num+k])
            
            seen[num] = min(seen[num], presum-num)
            
        return res if res > -inf else 0
