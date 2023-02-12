class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        axis = []
        presum = [0]
        for x, num in fruits:
            axis.append(x)
            presum.append(num+presum[-1])

        n = len(fruits)
        res = 0

        # go left and turn to right
        start = bisect.bisect_left(axis, startPos)
        for r in range(start, n):
            if axis[r] > startPos + k: break

            # length should: 2 * [l, startPos] + [startPos, r] <= k
            dist = (k-(axis[r] - startPos))//2
            leftPos = bisect.bisect_left(axis, startPos-dist)
            if leftPos < n:
                res = max(res, presum[r+1]-presum[leftPos])

        # go right and turn to left
        start = bisect.bisect_right(axis, startPos)-1 # > startPos的位置-1就是 >= startPos的位置
        r = n-1
        for l in range(start, -1, -1):
            if axis[l] < startPos - k: break
            
            # length constraint: 2 * [l, startPos] + [startPos, r] <= k
            dist = (k-(startPos-axis[l]))//2
            rightPos = bisect.bisect_right(axis, startPos+dist)-1
            if rightPos < n:
                res = max(res, presum[rightPos+1]-presum[l])
            
        return res
