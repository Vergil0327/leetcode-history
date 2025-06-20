class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        N = S = E = W = res = 0
        for d in s:
            if d == "N":
                N += 1
            elif d == "S":
                S += 1
            elif d == "E":
                E += 1
            else:
                W += 1

            x1, y1 = max(N, S), min(N, S)
            x2, y2 = max(E, W), min(E, W)

            kk = k
            d1 = min(y1, kk)
            y1 -= d1
            kk -= d1

            d2 = min(y2, kk)
            y2 -= d2
            kk -= d2

            res = max(res, x1 + x2 + d1 + d2 - y1 - y2)
        return res

# greedily replace lower frequency direction and calculate maximum Manhattan distance.
# each replacement can gain 1 more distince