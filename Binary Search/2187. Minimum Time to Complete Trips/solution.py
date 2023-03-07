class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()

        def check(currTime):
            trips = 0
            for t in time:
                if t > currTime: break
                trips += currTime//t
            return trips >= totalTrips

        l, r = 0, totalTrips*time[0]

        while l < r :
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l