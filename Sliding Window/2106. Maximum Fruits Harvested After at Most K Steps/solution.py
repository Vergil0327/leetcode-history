class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        axis = []
        presum = [0]
        for x, num in fruits:
            axis.append(x)
            presum.append(num+presum[-1])

        res = 0

        # go left and turn to right
        start = bisect.bisect_left(axis, startPos)
        l = 0
        for r in range(start, len(fruits)):
            # length should: 2 * [l, startPos] + [startPos, r] <= k
            while axis[l] <= startPos and (axis[r]-startPos) + 2 * (startPos-axis[l]) > k:
                l += 1
            if axis[l] <= startPos:
                res = max(res, presum[r+1]-presum[l])
            elif axis[r] <= startPos + k:
                res = max(res, presum[r+1]-presum[l])

        # go right and turn to left
        start = bisect.bisect_right(axis, startPos)-1 # > startPos的位置-1就是 >= startPos的位置
        r = len(fruits)-1
        for l in range(start, -1, -1):
            # length constraint: 2 * [l, startPos] + [startPos, r] <= k
            while axis[r] >= startPos and (startPos-axis[l]) + 2 * (axis[r]-startPos) > k:
                r -= 1
            if axis[r] >= startPos:
                res = max(res, presum[r+1]-presum[l])
            elif axis[l] >= startPos-k:
                res = max(res, presum[r+1]-presum[l])
        return res
