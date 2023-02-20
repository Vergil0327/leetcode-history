# Find Longest Common Prefix

"""
Intuition:

time complexity: O(mn)
space complexity: O(mn)

just like Leetcode 1143. Longest Common Subsequence, use dynamic programming to find longest length.

since subarray must be consecutive, we need to set dp[i][j] = 0 if nums1[i] != nums2[j].
and iterate through all the possibility to find the longest length
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        # dp[i][j] = maximum length of a subarray in both nums1[:i] and nums2[:j]
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i, n1 in enumerate(nums1, start=1):
            for j, n2 in enumerate(nums2, start=1):
                if n1 == n2:
                    dp[i][j] = dp[i-1][j-1]+1
                # else:
                #     dp[i][j] = 0
        return max(map(max, dp))

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        # manually shift to 1-indexed
        nums1 = [0] + nums1
        nums2 = [0] + nums2

        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # else:
                #     dp[i][j] = 0
        return max(map(max, dp))


"""
time complexity: O(mn)
space complexity: O(n)

since our `dp` only depends on previous row, we can reduce 2-D arrry to 1-D array
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        # dp[i][j] = maximum length of a subarray in both nums1[:i] and nums2[:j]
        # dp = [[0] * (n+1) for _ in range(m+1)]
        prevDp = [0] * (n+1)
        dp = [0] * (n+1)

        longest = 0
        for i, n1 in enumerate(nums1, start=1):
            for j, n2 in enumerate(nums2, start=1):
                if n1 == n2:
                    dp[j] = prevDp[j-1]+1 # dp[i][j] = dp[i-1][j-1]+1
                    longest = max(longest, dp[j])
                else:
                    dp[j] = 0 # dp[i][j] = 0
            prevDp, dp = dp, prevDp
            
        return longest


class SolutionTopDownTLE:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        @functools.lru_cache(None)
        def dfs(i, j, currLen):
            if i == m or j == n:
                return currLen
            
            maxLen = currLen
            if nums1[i] == nums2[j]:
                maxLen = max(maxLen, dfs(i+1, j+1, currLen+1))
            
            maxLen = max(maxLen, max(dfs(i+1, j, 0), dfs(i, j+1, 0)))
            
            return maxLen
        
        return dfs(0, 0, 0)
        