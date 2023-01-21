class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        
        minHeap = []
        res = currSum = 0
        for num, currMin in arr:
            heapq.heappush(minHeap, num)
            currSum += num
            if len(minHeap) > k:
                currSum -= heapq.heappop(minHeap)
            if len(minHeap) == k:
                res = max(res, currSum * currMin)
        return res