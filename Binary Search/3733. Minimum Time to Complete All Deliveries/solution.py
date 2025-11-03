from math import gcd
class Solution:
    def minimumTime(self, D: List[int], R: List[int]) -> int:
        def check(t):
            recharge_cnt1 = t // R[0]
            recharge_cnt2 = t // R[1]

            LCM = R[0] * R[1] // gcd(R[0], R[1])
            same_recharge_cnt = t // LCM
            
            return (t - recharge_cnt1 >= D[0] and
                    t - recharge_cnt2 >= D[1] and
                    t - same_recharge_cnt >= D[0] + D[1])

        l, r = sum(D), 10**12
        while l < r:
            mid = l + (r-l)//2

            if check(mid):
                r = mid
            else:
                l = mid+1
        return l