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

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        positions = []
        presum = [0]

        for pos, amt in fruits:
            positions.append(pos)
            presum.append(presum[-1]+amt)

        res = 0

        # to-left then to-right
        # X startPos X X X X X X X X => `positions` array
        #          <-i
        #          ->i ->->->  r
        i = bisect.bisect_left(positions, startPos)
        for r in range(i, n):
            if positions[r] > startPos+k: break

            dist = (k-(positions[r]-startPos))//2 # to-left back-and-forth
            l = bisect.bisect_left(positions, startPos-dist)

            res = max(res, presum[r+1]-presum[l])

        # to-right then to-left
        # X X X X X X X startPos X X X
        #             i ->
        #   l  <-<-<- i <-
        i = bisect.bisect_right(positions, startPos)-1
        for l in range(i, -1, -1):
            if positions[l] < startPos-k: break

            dist = (k-(startPos-positions[l]))//2 # to-right back-and-forth
            r = bisect.bisect_right(positions, startPos+dist)
            res = max(res, presum[r]-presum[l])

        return res
