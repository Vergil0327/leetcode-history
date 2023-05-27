class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        A, B = sum(nums1), sum(nums2)
        diff = A-B

        if diff == 0: return 0
        n, m = len(nums1), len(nums2)
        nums1.sort()
        nums2.sort()

        res = 0
        if diff > 0: # decrease A or increase B
            i = n-1
            j = 0
            while i >= 0 or j < m:
                dec = nums1[i]-1 if i >= 0 else 0
                inc = 6-nums2[j] if j < m else 0

                if dec > inc:
                    diff -= dec
                    i -= 1
                elif dec < inc:
                    diff -= inc
                    j += 1
                elif dec > 0:
                    diff -= dec
                    i -= 1
                elif inc > 0:
                    diff -= inc
                    j += 1
                else:
                    return -1
                    
                res += 1
                if diff <= 0: return res
            return -1
        else: # increase A or decrease B
            i = 0
            j = m-1
            while i < n or j >= 0:
                inc = 6-nums1[i] if i < n else 0
                dec = nums2[j]-1 if j >= 0 else 0

                if dec > inc:
                    diff += dec
                    j -= 1
                elif dec < inc:
                    diff += inc
                    i += 1
                elif dec > 0:
                    diff += dec
                    j -= 1
                elif inc > 0:
                    diff += inc
                    i += 1
                else:
                    return -1

                res += 1
                if diff >= 0: return res
            return -1

