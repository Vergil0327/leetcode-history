from sortedcontainers import SortedList
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        pre, suf = SortedList(), SortedList(arr)
        n = len(arr)
        res = 0
        for j in range(n):
            suf.remove(arr[j])
            l = pre.bisect_left(arr[j]-a)
            r = pre.bisect_right(arr[j]+a)

            l1 = suf.bisect_left(arr[j]-b)
            r1 = suf.bisect_right(arr[j]+b)

            for i in range(l, r):
                l2 = suf.bisect_left(pre[i]-c)
                r2 = suf.bisect_right(pre[i]+c)
                l2 = max(l1, l2)
                r2 = min(r1, r2)
                res += max(0, r2-l2)
            pre.add(arr[j])
        return res