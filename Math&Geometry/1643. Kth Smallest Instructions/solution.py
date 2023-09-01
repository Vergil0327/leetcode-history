class Solution:
    @cache
    def C(self, m, n):
        if n == 0:
            return 1
        elif m == 0:
            return 0
        else:
            # 一定取 + 一定不取
            return self.C(m-1, n-1) + self.C(m-1, n)
        

    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        V, H = destination[0], destination[1]
        n = V+H

        res = ""
        for i in range(n):
            if H == 0:
                res += "V"
                V -= 1
                continue
            if V == 0:
                res += "H"
                H -= 1
                continue

            comb = self.C(H-1+V, V)
            if comb >= k:
                H -= 1
                res += "H"
            else:
                V -= 1
                k -= comb
                res += "V"
        return res
