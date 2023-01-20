class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # (1-k) * int(n) = 1 - k ** digits
        # k ** digits = 1 - (1-k) * int(n) = 1 - int(n) + k * int(n)
        # digits_max = logk(int(n))

        digits_max = math.log(int(n), 2)
        for d in range(int(digits_max)+1, 1, -1):
            l, r = 2, int(n)-1
            while l <= r:
                k = l + (r-l)//2

                curr = 0
                for i in range(d):
                    curr += k ** i

                if curr == int(n): return str(k)
                elif curr > int(n):
                    r = k-1
                else:
                    l = k+1
        return -1