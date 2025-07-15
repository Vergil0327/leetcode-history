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
            p = partition(l, r)

            if p == target:
                return nums[p]
            elif p > target:
                return quickselect(l, p-1)
            else:
                return quickselect(p+1, r)
        return quickselect(0, len(nums)-1)
