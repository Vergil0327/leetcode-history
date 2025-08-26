class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        maxFromLeft = nums.copy()
        for i in range(1, n):
            maxFromLeft[i] = max(maxFromLeft[i-1], maxFromLeft[i])
        
        minFromRight = nums.copy()
        for i in range(n-2, -1, -1):
            minFromRight[i] = min(minFromRight[i+1], minFromRight[i])

        res = maxFromLeft.copy()
        for i in range(n-1, -1, -1):
            leftMax =  maxFromLeft[i]
            rightMin = minFromRight[i+1] if i+1<n else float('inf')
            if rightMin < leftMax:
                res[i] = max(res[i], res[i+1] if i+1 < n else -1)
        return res
