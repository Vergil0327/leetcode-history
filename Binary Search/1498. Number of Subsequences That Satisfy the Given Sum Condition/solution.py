class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        mod = 10**9 + 7

        res = 0
        for i in range(n):
            if nums[i] + nums[i] <= target:
                j = bisect.bisect_right(nums, target-nums[i])
                res += 2 ** (j-i-1)
                res %= mod
            else:
                break
        return res