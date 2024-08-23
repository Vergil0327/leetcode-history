class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        delta = mx = mn = 0
        for d in diff:
            delta += d
            mx = max(mx, delta)
            mn = min(mn, delta)

        if upper-lower < mx-mn: return 0
        return (upper-lower+1) - (mx-mn+1) + 1
