class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7
        index1 = {v: i for i, v in enumerate(nums1)}
        index2 = {v: i for i, v in enumerate(nums2)}
        n, m = len(nums1), len(nums2)

        common = deque()
        for i in range(n):
            if nums1[i] in index2:
                common.append(nums1[i])

        i = j = 0
        res = sum1 = sum2 = 0
        while common:
            num = common.popleft()
            ii = index1[num]
            jj = index2[num]
            while i <= ii:
                sum1 += nums1[i]
                i += 1
            while j <= jj:
                sum2 += nums2[j]
                j += 1

            res = (res + max(sum1, sum2))%mod
            sum1 = sum2 = 0

        while i < n:
            sum1 += nums1[i]
            i += 1
        while j < m:
            sum2 += nums2[j]
            j += 1
        res = (res + max(sum1, sum2))%mod

        return res

# Concise

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7
        sum1 = sum2 = res = 0
        i = j = 0
        n, m = len(nums1), len(nums2)
        while i < n or j < m:
            if j == m:
                sum1 += nums1[i]
                i += 1
            elif i == n:
                sum2 += nums2[j]
                j += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            elif nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            else: # common value position
                sum1 += nums1[i]
                sum2 += nums2[j]
                i, j = i+1, j+1

                res = (res + max(sum1, sum2)) % mod
                sum1 = sum2 = 0
        return (res + max(sum1, sum2))%mod