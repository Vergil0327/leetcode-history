class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        arr = set()
        cur = 1
        while len(arr) < n:
            if k-cur not in arr:
                arr.add(cur)
            cur += 1
        return sum(arr)
        