class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        def lcm(a, b):
            return a * b // gcd(a, b)
        LCM = lcm(divisor1, divisor2)

        l, r = 2, 2*(10**9)+1
        while l < r:
            mid = l + (r-l)//2
            # total available num: from 1 to N excluding LCM and its multiply
            total = mid - mid//LCM
            numArr1 = mid-mid//divisor1
            numArr2 = mid-mid//divisor2
            if total >= uniqueCnt1+uniqueCnt2 and numArr1 >= uniqueCnt1 and numArr2 >= uniqueCnt2:
                r = mid
            else:
                l = mid+1
        return l
