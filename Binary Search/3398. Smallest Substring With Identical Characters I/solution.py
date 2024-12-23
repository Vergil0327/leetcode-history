class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        arr = [len(list(consecutive)) for _, consecutive in groupby(s)]

        def check(limit):
            if limit == 1: # should be alternate "010101..." or "101010..."
                x = sum(int(ch) != i % 2 for i, ch in enumerate(s)) # check diff compared with "01010101..."
                # then, diff compared with "101010..." is len(s)-x
                return min(x, len(s) - x) <= numOps

            return sum(length//(limit+1) for length in arr) <= numOps

        l, r = 1, n
        while l < r:
            mid = l + (r-l)//2

            if check(mid):
                r = mid
            else:
                l = mid+1
        return l
