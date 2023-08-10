from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        arr = []
        for i in range(n):
            arr.append(nums1[i]-nums2[i])

        sl = SortedList()
        res = 0
        for i in range(n):
            res += sl.bisect_right(arr[i]+diff)
            sl.add(arr[i])
        return res
    
# Intuition

# nums1[i]-nums2[i] <= nums1[j]-nums2[j]+diff
# => arr[i] <= arr[j]+diff

# 所以我們可以遍歷j, 然後用bisect_right找出前面有多少個符合條件的arr[i]
# n = bisect_right(sorted(arr[:i+1]), arr[j]+diff)
# 那這樣對於當前arr[j]來說, 就能組成n個合法pairs