from math import gcd

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9+7

        lcm = a*b//gcd(a, b) # 最小公倍數
        l, r = 1, min(a*n, b*n)
        while l < r:
            mid = l + (r-l)//2
            if mid//a + mid//b - mid//lcm >= n:
                r = mid
            else:
                l = mid+1
        return l%mod