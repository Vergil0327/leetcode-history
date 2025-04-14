# Intution

找triplet => 直覺想到遍歷中間`arr[j]`, 那就可以得出相對應的arr[i], arr[k]的範圍
然後再根據arr[i]跟arr[k]的條件`|arr[i] - arr[k]| <= c`, 去進一步遍歷arr[i]來縮小arr[k]範圍, 去找有多少個合法arr[k]
那麼就能得到當前arr[i], arr[j]所對應的合法arr[k]數量

全部加總即為答案

```py
from sortedcontainers import SortedList
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        pre, suf = SortedList(), SortedList(arr)
        n = len(arr)
        res = 0
        # 遍歷triplet的中間arr[j]
        for j in range(n):
            suf.remove(arr[j])

            # |arr[i] - arr[j]| <= a
            # => arr[j]-a <= arr[i] <= arr[j]+a
            l1 = pre.bisect_left(arr[j]-a)
            r1 = pre.bisect_right(arr[j]+a)

            # |arr[j] - arr[k]| <= b
            # => arr[j]-b <= arr[k] <= arr[j]+b
            l21 = suf.bisect_left(arr[j]-b)
            r21 = suf.bisect_right(arr[j]+b)

            for i in range(l1, r1):
                # |arr[i] - arr[k]| <= c
                # arr[i]-c <= arr[k] <= arr[i]+c
                l22 = suf.bisect_left(pre[i]-c)
                r22 = suf.bisect_right(pre[i]+c)

                # arr[k]的合法範圍必須考慮到跟arr[i]以及arr[j]兩個條件
                l2 = max(l21, l22)
                r2 = min(r21, r22)
                res += max(0, r2-l2)
            pre.add(arr[j])
        return res
```