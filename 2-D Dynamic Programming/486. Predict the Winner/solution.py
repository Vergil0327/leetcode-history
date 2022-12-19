# optimized with Prefix Sum
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + nums[i-1]

        @lru_cache(None)
        def play(l, r): # the maximum score player1 can get
            if l == r: return nums[l]

            p2MaxIfP1TakeFirst = play(l+1, r)
            p2MaxIfP1TakeLast = play(l, r-1)

            # the max socre player1 can get = current choice + remain scores - max score player2 can get
            # we can take either first or last, we choose max
            player1Max = max(
                nums[l] + (presum[r+1] - presum[l+1]) - p2MaxIfP1TakeFirst,
                nums[r] + (presum[r] - presum[l]) - p2MaxIfP1TakeLast,
            )
            return player1Max

        player1Max = play(0, len(nums)-1)
        player2Max = presum[n] - player1Max
        return  player1Max >= player2Max

# Brute Force
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def play(l, r): # the maximum score player1 can get
            if l == r: return nums[l]

            # the max socre player1 can get = current choice + remain scores - max score player2 can get
            player1 = max(nums[l] + sum(nums[l+1:r+1]) - play(l+1, r), nums[r] + sum(nums[l:r]) - play(l, r-1))
            return player1

        player1Max = play(0, len(nums)-1)
        return  player1Max >= sum(nums) - player1Max