class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        for i in range(n):
            if s[i] == "R":
                nums[i] += d
            else:
                nums[i] -= d

        nums.sort()
        l, r = 0, n-1
        res = 0
        while l < r:
            res += (nums[r]-nums[l]) * (r-l)
            res %= mod
            l, r = l+1, r-1

        # or prefix sum
        # nums.sort()
        # res = 0
        # presum = [0] + list(accumulate(nums))
        # for i in range(1, n):
        #     res += i * nums[i] - presum[i]
        #     res %= mod
        # return res
        return res
