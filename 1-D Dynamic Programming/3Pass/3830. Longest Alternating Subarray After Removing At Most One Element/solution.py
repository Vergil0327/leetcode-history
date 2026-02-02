"""
This problem is a variation of the "Longest Alternating Subarray" problem, but with the added complexity of allowing at most one removal.

The most efficient way to solve this is using Dynamic Programming with a Left-Right pass (often called the "Bridge" or "Pivot" technique).
We calculate the longest alternating sequences ending at each index and starting at each index, then try to "bridge" them by removing a single element.

1. The Strategy

- Precompute Left DP (L[i][type]): The length of the longest alternating subarray ending at index i.

    - L[i][0]: Last comparison was nums[i-1] < nums[i] (Up).

    - L[i][1]: Last comparison was nums[i-1] > nums[i] (Down).

- Precompute Right DP (R[i][type]): The length of the longest alternating subarray starting at index i.

    - R[i][0]: First comparison is nums[i] < nums[i+1] (Up).

    - R[i][1]: First comparison is nums[i] > nums[i+1] (Down).

- Bridge the Gap: Iterate through the array and imagine removing nums[i]. Check if nums[i-1] and nums[i+1] can form a valid alternating connection.
"""

class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        
        # left[i][0] ends in < (increasing), left[i][1] ends in > (decreasing)
        left = [[1, 1] for _ in range(n)]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                left[i][0] = left[i-1][1] + 1
            elif nums[i] < nums[i-1]:
                left[i][1] = left[i-1][0] + 1
        
        # right[i][0] starts with < (increasing), right[i][1] starts with > (decreasing)
        right = [[1, 1] for _ in range(n)]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                right[i][0] = right[i+1][1] + 1
            elif nums[i] > nums[i+1]:
                right[i][1] = right[i+1][0] + 1
                
        # Base case: Max length without removing any element
        ans = 0
        for i in range(n):
            ans = max(ans, left[i][0], left[i][1])
            
        # Try removing each element at index i to join left[i-1] and right[i+1]
        for i in range(1, n - 1):
            # Case 1: nums[i-1] < nums[i+1]
            # To be valid: [... > nums[i-1]] < [nums[i+1] > ...]
            if nums[i-1] < nums[i+1]:
                ans = max(ans, left[i-1][1] + right[i+1][1])
                
            # Case 2: nums[i-1] > nums[i+1]
            # To be valid: [... < nums[i-1]] > [nums[i+1] < ...]
            if nums[i-1] > nums[i+1]:
                ans = max(ans, left[i-1][0] + right[i+1][0])
                
        return ans