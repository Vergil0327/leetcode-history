from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        mapping = {nums1[i]: i for i in range(n)}
        for i in range(n):
            nums2[i] = mapping[nums2[i]]
        
        smallerBefore, arr = [], SortedList()
        for i in range(n):
            cnt = arr.bisect_left(nums2[i])
            smallerBefore.append(cnt)
            arr.add(nums2[i])
        
        res = 0
        for i in range(n):
            smallerAfterSelf = nums2[i] - smallerBefore[i]
            largerAfterSelf = n-i-1 - smallerAfterSelf
            res += smallerBefore[i] * largerAfterSelf
        return res