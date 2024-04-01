def findMaxManhattan(arr, skip=-1):
    maxSum = maxDiff = -inf
    minSum = minDiff = inf
    for i in range(len(arr)):
        if i == skip: continue

        s = sum(arr[i])
        d = arr[i][0]-arr[i][1]
        maxSum = max(maxSum, s)
        minSum = min(minSum, s)
        maxDiff = max(maxDiff, d)
        minDiff = min(minDiff, d)
    return max(maxSum-minSum, maxDiff - minDiff)

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0]+x[1])
        res = min(findMaxManhattan(points[1:]), findMaxManhattan(points[:-1]))

        points.sort(key=lambda x: x[0]-x[1])
        res = min(res, min(findMaxManhattan(points[1:]), findMaxManhattan(points[:-1])))

        return res