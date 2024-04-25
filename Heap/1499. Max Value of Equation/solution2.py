class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = deque()
        res = -inf
        for x, y in points:
            while queue and x-queue[0][1] > k: # pop invalid point[i]
                queue.popleft()

            # find max result here
            if queue:
                res = max(res, queue[0][0] + x + y)

            while queue and queue[-1][0] <= y-x: # monotonically decreasing
                queue.pop()
            queue.append([y-x, x])
        return res