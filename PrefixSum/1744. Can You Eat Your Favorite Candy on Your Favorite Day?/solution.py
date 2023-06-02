class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + candiesCount[i-1]

        res = []
        for t, d, cap in queries:
            l, r = d+1, cap*(d+1)
            i = bisect.bisect_left(presum, l)
            j = bisect.bisect_left(presum, r)
            res.append(i-1 <= t <= j-1)
        return res