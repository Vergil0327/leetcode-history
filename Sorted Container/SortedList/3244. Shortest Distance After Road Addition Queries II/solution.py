from sortedcontainers import SortedList
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        sl = SortedList(range(n))
        for u, v in queries:
            i = sl.bisect_left(u)
            j = sl.bisect_right(v)-1
            if sl[i] == u:
                i += 1
            if sl[j] == v:
                j -= 1
            for _ in range(j-i+1):
                sl.pop(i)

            res.append(len(sl)-1)
        return res

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        union = {i: i + 1 for i in range(n - 1)} # i -> i+1 for 0 <= i < n initially

        res = []
        for u, v in queries:
            # delete [u+1, v-1] interval
            if u in union and union[u] < v:
                start = u
                while start < v:
                    start = union.pop(start)
                union[u] = v

            res.append(len(union))
        return res