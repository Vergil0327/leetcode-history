# Array & Hashing
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        has = defaultdict(int)

        for num in sorted(set(nums), reverse=True):
            n = num
            if n**2 in has:
                while n*n in has:
                    n= n*n
                has[n] += 1

            if num not in has:
                has[num] += 1
        longest = max(has.values())
        return longest if longest > 1 else -1

# DP
class Solution_Optimized:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        nums.sort()
        for num in nums:
            root = sqrt(num)
            if root*root == num:
                dp[num] = 1 + dp[root]
            else:
                dp[num] = 1
        longest = max(dp.values())
        return longest if longest > 1 else -1