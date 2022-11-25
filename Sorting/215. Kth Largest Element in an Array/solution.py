class QuickSelectSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            p = l
            pivot = nums[r]
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            return p
        
        target = len(nums)-k
        def quickselect(l, r):
            # if l >= r: return nums[l] # don't need it
            p = partition(l, r)

            if p == target:
                return nums[p]
            elif p > target:
                return quickselect(l, p-1)
            else:
                return quickselect(p+1, r)
        return quickselect(0, len(nums)-1)

class HeapSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        
        while k-1 > 0:
            heapq.heappop(maxHeap)
            k -= 1
        return -maxHeap[0]