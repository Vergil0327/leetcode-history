class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        
        heapq.heapify(nums)
        dev = mx-nums[0]
        while nums[0]%2==1:
            v = heapq.heappop(nums)
            v *= 2
            if v < mx:
                heapq.heappush(nums, v)
                dev = min(dev, mx-nums[0])
            else:
                mx = v
                heapq.heappush(nums, v)
                dev = min(dev, mx-nums[0])
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)

        mn = nums[0]
        while (-maxHeap[0])%2 == 0:
            v = -heapq.heappop(maxHeap)
            v //= 2
            if v > mn:
                heapq.heappush(maxHeap, -v)
                dev = min(dev, -maxHeap[0]-mn)
            else:
                mn = v
                heapq.heappush(maxHeap, -v)
                dev = min(dev, -maxHeap[0]-v)
        return dev