class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        inf = float("inf")
        
        histogram = [-inf] + [0 for i in range(len(matrix[0]))] + [-inf]
        maxRec = 0
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "0":
                    histogram[c+1] = 0
                else:
                    histogram[c+1] += 1
            
            # leetcode 84.
            # caluculate histogram: height * (nextSmaller[i]-prevSmaller[i]-1)
            stack = []
            for i in range(len(histogram)):
                while stack and histogram[stack[-1]] > histogram[i]:
                    index = stack.pop()
                    prevSmall, nextSmall = stack[-1], i
                    maxRec = max(maxRec, (nextSmall-prevSmall-1)*histogram[index])
                stack.append(i)

        return maxRec