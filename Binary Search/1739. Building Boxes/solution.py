class Solution:
    def minimumBoxes(self, n: int) -> int:
        def cal(area):
            d = floor((-1 + sqrt(1 + 4 * 2*area))/2)
            remain = area - (1+d)*d//2

            rows = [0] * d
            for i in range(d):
                rows[i] = d-i
            for i in range(remain):
                rows[i] += 1

            total = sufsum = 0
            for i in range(d-1, -1, -1):
                sufsum += rows[i]
                total += sufsum
            return total

        l, r = 1, int(1e9) # area: 1 <= n <= 10^9
        while l < r:
            mid = l + (r-l)//2
            if cal(mid) >= n:
                r = mid
            else:
                l = mid+1
        return l
