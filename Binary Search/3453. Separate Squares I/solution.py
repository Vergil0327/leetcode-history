class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def check(t):
            lower = upper = 0.0
            for x1, y1, l in squares:
                y2 = y1+l

                if y2 <= t:
                    lower += l*l
                elif y1 >= t:
                    upper += l*l
                else:
                    upper += l * abs(y2-t)
                    lower += l * abs(t-y1)

            return lower, upper


        l, r = 0, 10**10
        for _, y, l in squares:
            l = min(l, y)
            r = max(r, y+l)
        
        while r-l >= 1e-5:
            mid = (r - (r-l)/2)
            sumL, sumU = check(mid)
            
            if sumL >= sumU:
                r = mid
            elif sumL < sumU:
                l = mid

        return l