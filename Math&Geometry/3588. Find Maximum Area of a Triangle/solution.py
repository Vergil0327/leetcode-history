class Solution:
    def maxArea(self, coords: List[List[int]]) -> int:
        n = len(coords)

        # sort by `(coords[pos], coords[1-pos]) where pos in {0,1}`
        def check(pos):
            coords.sort(key=lambda x: (x[pos], x[1-pos]))

            maxRight = [-inf] * (n+1)
            minRight = [inf] * (n+1)
            for i in range(n-1, -1, -1):
                maxRight[i] = max(maxRight[i+1], coords[i][pos])
                minRight[i] = min(minRight[i+1], coords[i][pos])

            maxLeft = -inf
            minLeft = inf
            res = -1
            i = j = 0
            while i < n:
                j = i

                x = coords[i][pos]
                while j < n and coords[j][pos] == x:
                    j += 1

                if j == i:
                    maxLeft = max(maxLeft, x)
                    minLeft = min(minLeft, x)
                    i = j+1
                    continue

                j -= 1
                base = coords[j][1-pos] - coords[i][1-pos]
                height = max(maxRight[i+1]-x, x-minRight[i+1], maxLeft-x, x-minLeft)
                if (ans:=base*height) > 0:
                    res = max(res, ans)

                maxLeft = max(maxLeft, x)
                minLeft = min(minLeft, x)
                i = j+1
            return res
        
        return max(check(0), check(1))