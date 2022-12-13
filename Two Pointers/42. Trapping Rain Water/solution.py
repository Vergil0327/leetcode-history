class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i-1])

        rightMax = [0] * n
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])

        water = 0
        for i in range(n):
            diffHei = min(leftMax[i], rightMax[i])-height[i]
            water += max(0, diffHei)
        return water