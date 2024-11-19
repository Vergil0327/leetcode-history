class Solution:
    def minDifference(self, A: List[int]) -> int:
        groups = [list(grp) for k, grp in groupby(A, key=lambda x: x>0)]
        singles = []  # a? or a??
        doubles = []  # a?b or a??b
        base = 0  # the max diff of two positive elements

        for i, grp in enumerate(groups):
            if grp[0] != -1:
                for j in range(len(grp) - 1):
                    base = max(base, abs(grp[j] - grp[j+1]))
                continue

            neighbors = []
            if i - 1 >= 0:
                neighbors.append(groups[i-1][-1])
            if i + 1 < len(groups):
                neighbors.append(groups[i+1][0])
            neighbors.sort()

            if len(neighbors) == 1:
                singles.append([*neighbors, len(grp) > 1])
            if len(neighbors) == 2:
                doubles.append([*neighbors, len(grp) > 1])

        if not singles and not doubles:
            return base

        def possible(d):
            intervals = []
            for num, len2 in singles:
                intervals.append([num-d, num+d])

            for num1, num2, len2 in doubles:
                if len2:
                    intervals.append([num1-d, num1+d])
                    intervals.append([num2-d, num2+d])
                else:
                    lo = num2 - d
                    hi = num1 + d
                    if lo > hi: return 0
                    intervals.append([lo, hi])

            # we have a bunch of intervals, and we want to know if we can stab twice
            # to hit all intervals
            lo = min(e for s,e in intervals)
            hi = max(s for s,e in intervals)
    
            if lo + d < hi:
                if not all(
                    any(abs(a-p) <= d and abs(b-p) <= d for p in [lo, hi]) 
                    for a,b,_ in doubles
                ):
                    return 0

            return all(s <= lo <= e or s <= hi <= e for s,e in intervals)
            
        return bisect_left(range(10**9), 1, base, max(A), key=possible)
 