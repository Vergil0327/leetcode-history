class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        dp = set([nums[0]])
        res = abs(k - nums[0])
        for num in nums:
            dp = set([num] + [num & x for x in dp])
            for x in dp:
                res = min(res, abs(k - x))
        return res
