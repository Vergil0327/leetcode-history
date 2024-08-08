# credit to @sgallivan
class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        parent = list(range((n := len(circles)) + 2))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(n):
            x, y, r = circles[i]
            if (x - X) ** 2 + (y - Y) ** 2 <= r ** 2:               # Early exit 1
                return False                                        #   if circle overlaps exit
            if (x <= r and y <= Y) or (y + r >= Y and x <= X):
                parent[find(n)] = find(i)
            if (y <= r and x <= X) or (x + r >= X and y <= Y):
                parent[find(n + 1)] = find(i)
            if find(n) == find(n + 1):                              # Early exit 2
                return False                                        #   if circle touches both borders

        if find(n) == n or find(n + 1) == n + 1:                    # Early exit 3
            return True                                             #   if either border is untouched

        for i in range(n):
            x, y, r = circles[i]
            if x - r >= X or y - r >= Y or (x >= X and y >= Y):     # Circle 1 out of usable range
                continue

            for j in range(i):
                if find(i) == find(j):                              # Skip if already unioned
                    continue

                x2, y2, r2 = circles[j]
                if (x + x2) / 2 >= X and (y + y2) / 2 >= Y:         # Circle pair out of usable range
                    continue

                if (x - x2) ** 2 + (y - y2) ** 2 <= (r + r2) ** 2:  # Circles intersect
                    parent[find(i)] = find(j)
                    if find(n) == find(n + 1):                      # Early exit 4
                        return False                                #   if both borders are unioned
        return True
