# O(M * M * N * N * logN) or O(N * N * M * M * logM)
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def helper(nums, k):
            n = len(nums)

            # currSum - presum[i] <= k
            # find a presum[i] >= currSum - k
            res, currSum = -inf, 0
            presum = [0]
            for i in range(n):
                currSum += nums[i]
                idx = bisect.bisect_left(presum, currSum-k)
                if idx != len(presum):
                    res = max(res, currSum - presum[idx])

                bisect.insort_left(presum, currSum) # O(n). we can use sortedcontainers to reduce this step to O(logn)
                
            return res

        m, n = len(matrix), len(matrix[0])
        if m > n:
            transpose = list(zip(*matrix)) # *matrix = matrix... in Javasciprt (spread operator)
            return self.maxSumSubmatrix(transpose, k) # change time complexity to N * N * M * M * logM

        maxSum = -inf
        for i in range(m):
            presum = [0] * n
            for j in range(i, m):
                for p in range(n):
                    presum[p] += matrix[j][p]
                maxSum = max(maxSum, helper(presum, k))
        return maxSum

# TLE, (M^2 * N^2 + M*N)
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        squarePresum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                squarePresum[i+1][j+1] = squarePresum[i+1][j] + squarePresum[i][j+1] + matrix[i][j] - squarePresum[i][j]
        maxSum = -inf
        for y1 in range(m+1):
            for y2 in range(y1+1, m+1):
                for x1 in range(n+1):
                    for x2 in range(x1+1, n+1):
                        total = squarePresum[y2][x2] - squarePresum[y2][x1] - squarePresum[y1][x2] + squarePresum[y1][x1]
                        if total == k: return k
                        if total < k and total > maxSum:
                            maxSum = max(maxSum, total)
        return maxSum