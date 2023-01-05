class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        base = nums[0]
        moves = 0
        for i in range(1, len(nums)):
            moves += nums[i]-base
        return moves