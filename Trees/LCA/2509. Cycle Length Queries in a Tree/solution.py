class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        for u, v in queries:
            if u < v:
                u, v = v, u
            
            path = set()
            length = 0
            vIsLCA = False
            while u != 1 and u != v:
                length += 1
                u //= 2
                path.add(u)
                if u == v:
                    vIsLCA = True

            if not vIsLCA:
                while v != 1 and v not in path:
                    length += 1
                    v //= 2

                while v != 1:
                    length -= 1
                    v //= 2
            res.append(length + 1)
        return res

class ConciseSolution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        for u, v in queries:
            length = 1 # added edge
            while u != v: # find way back until reach LCA
                if v > u:
                    v //= 2
                else:
                    u //= 2
                length += 1
            res.append(length)
        return res
