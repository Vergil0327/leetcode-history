class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(1 for num in nums if num == 0)
        
        n = len(nums)
        diff = [0] * (n+1) # use difference array for accumulated flips

        res = 0
        for i in range(n-k+1):
            diff[i] += diff[i-1]

            if (nums[i]+diff[i])%2 == 0:
                diff[i] += 1
                diff[i+k] -= 1
                res += 1

        for i in range(n-k+1, n):
            diff[i] += diff[i-1]

            if (nums[i]+diff[i])%2 == 0:
                return -1
        return res
