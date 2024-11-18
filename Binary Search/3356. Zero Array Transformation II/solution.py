class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def check(k):
            diff = [0] * (n+1)
            for i in range(0, k):
                l, r, val = queries[i]
                diff[l] += val
                diff[r+1] -= val

            for i in range(1, n+1):
                diff[i] += diff[i-1]

            return all(nums[i] - diff[i] <= 0 for i in range(n))

        l, r = 0, len(queries)
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l if check(l) else -1
