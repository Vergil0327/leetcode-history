class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        
        minHeap = [] # [product of ui * vi, ui, vi] [product, nums1[i], index/pointer of nums2]
        for i in range(m):
            minHeap.append([nums1[i]+nums2[0], nums1[i], 0])
        heapq.heapify(minHeap)

        res = []
        while minHeap and len(res) < k:
            _, num1, currIdx = heapq.heappop(minHeap)
            res.append((num1, nums2[currIdx]))
            
            nextNum2Idx = currIdx + 1
            if nextNum2Idx < n:
                heapq.heappush(minHeap, [num1+nums2[nextNum2Idx], num1, nextNum2Idx])
        return res