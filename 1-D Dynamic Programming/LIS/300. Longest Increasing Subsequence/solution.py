# Bottom-Up
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = length of LIS
        dp = [1] * len(nums)
        
        maxLen = 1
        n = len(nums)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i] == dp[j]+1:
                        maxLen = max(maxLen, dp[i])
        return maxLen

# Bottom-Up Optimized (Greedy, Patience Sort)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        n = len(nums)
        for i in range(n):
            idx = bisect.bisect_left(tails, nums[i])

            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
        return len(tails)

class SolutionTopDown:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        n = len(nums)
        memo = {}
        def dfs(i):
            if i == n: return 1
            
            if i in memo: return memo[i]
            
            res = []
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    res.append(dfs(j) + 1)
            
            memo[i] = max(res) if res else 1
            return memo[i]
        
        ans = []
        for i in range(n):
            ans.append(dfs(i))
        return max(ans) if ans else 1

def bisect_left(tails, num):
    l, r = 0, len(tails)
    while l < r:
        mid = l + (r-l)//2
        if tails[mid] < num:
            l = mid+1
        else:
            r = mid
    return l

def bisect_right(tails, num):
    l, r = 0, len(tails)
    while l < r:
        mid = l + (r-l)//2
        if tails[mid] > num:
            r = mid
        else:
            l = mid+1
    return l