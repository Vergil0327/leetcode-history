class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        l, r = 0, 1
        while True:
            mid = (l+r)/2

            border = [bisect.bisect(arr, arr[i]/mid) for i in range(n)]
            count = sum(n-j for j in border)

            if count > k:
                r = mid
            elif count < k:
                l = mid
            else:
                nums = [[arr[i], arr[j]] for i, j in enumerate(border) if j < n]
                return max(nums, key=lambda x:x[0]/x[1])
