class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)

        arr = [[num, i] for i, num in enumerate(nums1)]
        arr.sort()

        minHeap = []
        res = [0] * n
        maxSum = j = 0
        for i in range(n):
            while j < i and arr[j][0] < arr[i][0]:
                maxSum += nums2[arr[j][1]]
                heapq.heappush(minHeap, nums2[arr[j][1]])
                j += 1
            while len(minHeap) > k:
                maxSum -= heapq.heappop(minHeap)

            res[arr[i][1]] = maxSum
        return res
