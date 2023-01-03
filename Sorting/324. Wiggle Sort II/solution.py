# Space O(n)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = sorted(nums, reverse=True)
        first, second = a[:n//2], a[n//2:]
        
        for i in range(0, n, 2):
            nums[i] = second[i//2]
        for i in range(1, n, 2):
            nums[i] = first[(i-1)//2]

# we can also use third argument of array slice and assign array directly
# nums[start:end:step]
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        a = sorted(nums, reverse=True)

        first, second = a[:n//2], a[n//2:]
        nums[::2] = second
        nums[1::2] = first

# Concise Pythonic code
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums[::2])
        nums[::2], nums[1::2] = nums[:n][::-1], nums[n:][::-1]


# Quickselect O(n)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        def quickselect(l, r, k):
            if l == r: return nums[l]

            # random choose pivot
            pivotIdx = randint(l, r)
            nums[pivotIdx], nums[r] = nums[r], nums[pivotIdx]
            
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p < k:
                return quickselect(p+1, r, k)
            else:
                return quickselect(l, p-1, k)

        # O(n)
        median = quickselect(0, len(nums)-1, len(nums)//2)

        n = len(nums)
        res = [0] * n
        
        j = n-2 if n%2 == 0 else n-1
        k = 1
        for i in range(n):
            if nums[i] > median:
                res[k] = nums[i]
                k += 2
                continue

            if nums[i] < median:
                res[j] = nums[i]
                j -= 2
                continue
        
        while j >= 0:
            res[j] = median
            j -= 2
        while k < n:
            res[k] = median
            k += 2
        
        for i in range(n):
            nums[i] = res[i]
