from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        l, r = 0, 0
        window = SortedList()
        while r < len(nums):
            v = nums[r]
            r += 1
            
            window.add(v)
            while r-l >= k:
                if k&1:
                    res.append(window[k//2])
                else:
                    res.append((window[k//2] + window[k//2-1])/2)
                
                val = nums[l]
                l += 1
                window.remove(val)
        return res

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        l, r = 0, 0
        window = []
        while r < len(nums):
            v = nums[r]
            r += 1
            
            bisect.insort_left(window, v)
            while r-l >= k:
                if k&1:
                    res.append(window[k//2])
                else:
                    res.append((window[k//2] + window[k//2-1])/2)
                
                val = nums[l]
                idx = bisect.bisect_left(window, val)
                window.pop(idx)
                l += 1
                
        return res

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        l, r = 0, 0
        
        # value in minH > value in maxH
        minH = [] # larger value
        maxH = [] # smaller value
        
        while r < len(nums):
            v = nums[r]
            
            heapq.heappush(minH, v)
            if minH and maxH and minH[0] < -maxH[0]:
                v = heapq.heappop(minH)
                heapq.heappush(maxH, -v)
            
            # TRICKS: keeps len(maxH) >= len(minH)
            # median always be -maxH[0] if k is odd else (minH[0] + -maxH[0])/2
            while len(maxH)<len(minH) or len(maxH)>len(minH)+1:
                if len(maxH)>len(minH)+1:
                    removedMaxHeapItem = -heapq.heappop(maxH)
                    heapq.heappush(minH, removedMaxHeapItem)
                else:
                    removedMaxHeapItem = heapq.heappop(minH)
                    heapq.heappush(maxH, -removedMaxHeapItem)

            r += 1

            while r-l >= k:
                median = 0
                if k&1:
                    median = -maxH[0]
                    res.append(median)
                else:
                    median = (minH[0] + -maxH[0])/2
                    res.append(median)
                
                removed = nums[l]
                if removed<=median:
                    maxH.remove(-removed)
                    heapq.heapify(maxH)
                else:
                    minH.remove(removed)
                    heapq.heapify(minH)
                
                l += 1
                
        return res