class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        def canUseEveryBall(force):
            start = position[0]
            cnt = 1
            for i in range(n):
                if position[i]-start >= force:
                    cnt += 1
                    start = position[i]
            return cnt >= m

        
        l, r = 1, max(position)
        while l < r:
            mid = r - (r-l)//2
            if canUseEveryBall(mid):
                l = mid
            else:
                r = mid-1
        return l
