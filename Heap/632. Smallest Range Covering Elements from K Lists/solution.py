class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        ranges = [inf, -inf]
        for i in range(len(nums)):
            ranges[0] = min(ranges[0], nums[i][0])
            ranges[1] = max(ranges[1], nums[i][0])
            heapq.heappush(minHeap, [nums[i][0], 0, i])

        res = ranges.copy()
        while minHeap:
            _, i, j = heapq.heappop(minHeap) # nums[j][i], 第j條的第i個元素
            if i+1 < len(nums[j]):
                heapq.heappush(minHeap, [nums[j][i+1], i+1, j])
            else:
                break

            ranges[0] = minHeap[0][0]
            ranges[1] = max(ranges[1], nums[j][i+1])
            if ranges[1]-ranges[0] < res[1]-res[0]:
                res[0] = ranges[0]
                res[1] = ranges[1]
        return res
