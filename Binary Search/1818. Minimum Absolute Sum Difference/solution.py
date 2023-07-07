class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums1)
        snums1 = sorted(nums1)

        maxReducedDiff = 0
        total = 0
        for i in range(n):
            origin = abs(nums1[i]-nums2[i])
            total += origin
            
            j = bisect.bisect_left(snums1, nums2[i])
            l, r = j-1, j
            if l >= 0:
                replace = abs(nums2[i] - snums1[l])
                if replace < origin:
                    maxReducedDiff = max(maxReducedDiff, origin-replace)
            if r < n:
                replace = abs(nums2[i] - snums1[r])
                if replace < origin:
                    maxReducedDiff = max(maxReducedDiff, origin-replace)
        return (total - maxReducedDiff)%mod

