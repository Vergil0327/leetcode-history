class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        left, right = [], []
        for i in range(k):
            l2r, pick, r2l, put = time[i]
            effeciency = l2r+r2l
            heapq.heappush(left, [-effeciency, -i])
        
        currTime = 0
        picking = []
        putting = []
        while n:
            if right:
                # corss bridge: R -> L Putting
                eff, i = heapq.heappop(right)
                currTime += time[-i][2]

                heapq.heappush(putting, [currTime+time[-i][3], eff, i])
            elif left:
                # corss bridge: L -> R Picking
                eff, i = heapq.heappop(left)
                currTime += time[-i][0]
                n -= 1

                heapq.heappush(picking, [currTime+time[-i][1], eff, i])
            else:
                # find one who's ready to cross the bridge
                if not putting:
                    currTime = picking[0][0]
                elif not picking:
                    currTime = putting[0][0]
                else:
                    currTime = min(picking[0][0], putting[0][0])

            # now, current time is the most recent work to finish
            # these are ready to cross the bridge in left or right
            while picking and picking[0][0] <= currTime:
                _, eff, i = heapq.heappop(picking)
                heapq.heappush(right, [eff, i])
            while putting and putting[0][0] <= currTime:
                _, eff, i = heapq.heappop(putting)
                heapq.heappush(left, [eff, i])
        
        # some in right and some in picking
        # we need to send them back

        # right cross first
        while right:
            eff, i = heapq.heappop(right)
            currTime += time[-i][2]
            while picking and picking[0][0] <= currTime:
                _, eff, i = heapq.heappop(picking)
                heapq.heappush(right, [eff, i])

        # last few workers
        while picking:
            endTime, eff, i = heapq.heappop(picking)
            currTime = max(currTime, endTime)

            # to right then to left
            # _, eff, i = heapq.heappop(picking)
            # heapq.heappush(right, [eff, i])
            # while right:
            #     eff, i = heapq.heappop(right)
            #     currTime += time[-i][2]
            currTime += time[-i][2]
            # we don't need to increment putNew time at final round

        return currTime
