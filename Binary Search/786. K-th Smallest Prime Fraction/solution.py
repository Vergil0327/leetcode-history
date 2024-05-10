class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        l, r = 0, 1
        while l <= r:
            mid = l + (r-l)/2

            # arr[i]/arr[j] <= mid => arr[j] >= arr[i]/mid
            border = [bisect.bisect(arr, arr[i]/mid) for i in range(n)]
            count = sum(n-j for j in border)

            if count > k:
                r = mid
            elif count < k:
                l = mid
            else:
                # 此時恰好k個pairs
                # k-th pair就是這k個pairs中最大的那個
                pairs = [[arr[i], arr[j]] for i, j in enumerate(border) if j < n]
                return max(pairs, key=lambda x:x[0]/x[1])
