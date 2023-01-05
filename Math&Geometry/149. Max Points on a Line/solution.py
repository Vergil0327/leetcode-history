# Brute Force
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        count = defaultdict(set)

        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                # y = mx + b
                m = (y2-y1)/(x2-x1) if x2-x1 != 0 else inf
                b = y1-m*x1 if m != inf else x1
                count[(m,b)].add(tuple(points[i]))
                count[(m,b)].add(tuple(points[j]))

        return max([len(v) for v in count.values()] or [1])

# Better
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1: return 1
        
        res = 0
        for i in range(n):
            x1, y1 = points[i]
            count = defaultdict(int)

            for j in range(i + 1, n):
                x2, y2 = points[j]

                # y = mx + b
                dy, dx = y2-y1, x2-x1
                sign = 1 if dx * dy > 0 else -1
                GCD = gcd(dy, dx)
                if dx != 0:
                    m = f"{sign}{abs(dy//GCD)}/{abs(dx//GCD)}"
                    count[m] += 1
                else:
                    count["inf"] += 1

            res = max(res, max(count.values() or [0]) + 1)
        return res