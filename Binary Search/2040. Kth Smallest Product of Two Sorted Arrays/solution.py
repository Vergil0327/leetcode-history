class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count(m):
            cnt = 0
            for num in nums1:
                if num > 0:
                    # num * nums2[j] <= m
                    # nums2[j] <= m/num
                    # [0,j]都是符合的
                    cnt += bisect_right(nums2, floor(m/num))
                elif num < 0:
                    # num * nums2[j] > m
                    # nums2[j] > m/num
                    # [ceil(m/num), nums2[-1]] 都是符合的 => [j, n-1]
                    cnt += len(nums2)-bisect_left(nums2, ceil(m/num))
                else: # product == 0
                    if m >= 0:
                        cnt += len(nums2)
            return cnt


        l, r = int(-1e10), int(1e10)
        while l < r:
            mid = l + (r-l)//2
            if count(mid) < k:
                l = mid+1
            else:
                r = mid
        return l
