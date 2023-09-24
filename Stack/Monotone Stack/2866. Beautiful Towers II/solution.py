class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
            
        left = [0] * n
        stack = [-1]
        for i in range(n):
            while len(stack) > 1 and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            j = stack[-1]
            left[i] = (i-j) * maxHeights[i] + (left[j] if j >= 0 else 0)
            stack.append(i)

        right = [0] * n
        stack = [n]
        for i in range(n-1, -1, -1):
            while len(stack)> 1 and maxHeights[stack[-1]] >= maxHeights[i]:
                stack.pop()
            j = stack[-1]
            right[i] = (j-i) * maxHeights[i] + (right[j] if j < n else 0)
            stack.append(i)

        res = 0
        for i in range(n):
            res = max(res, left[i]+right[i]-maxHeights[i])
        return res