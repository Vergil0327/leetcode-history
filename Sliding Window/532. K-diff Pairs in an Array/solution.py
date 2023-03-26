class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = r = 0
        n = len(nums)
        SET = set()
        while r < n:
            num = nums[r]
            r += 1

            while l < r and num - nums[l] > k:
                l += 1
            if l != r-1 and num - nums[l] == k:
                SET.add((nums[l], num))

        return len(SET)