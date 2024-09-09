class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def check(score):
            n = len(start)
            l = start[0]
            for i in range(1, n):
                ll, rr = start[i], start[i]+d
                if (target := l+score) > rr: return False

                if target < ll:
                    l = ll
                else:
                    l = target
            return True
        
        l, r = 0, start[-1]+d-start[0]
        while l < r:
            mid = r - (r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l