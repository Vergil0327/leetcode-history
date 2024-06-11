class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(k+1)]
        max_dp_so_far = [0]*(k+1)

        for i in range(n):
            for j in range(k, -1, -1):
                dp[j][nums[i]] = max(dp[j][nums[i]]+1, max_dp_so_far[j-1]+1 if j-1>=0 else 0)
                max_dp_so_far[j] = max(max_dp_so_far[j], dp[j][nums[i]])
        return max(max_dp_so_far)
