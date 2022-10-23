class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = sorted(nums)[len(nums)//2]
        return sum(abs(median-num) for num in nums)