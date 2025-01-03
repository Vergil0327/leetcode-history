class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1

        while l <= r:
            mid = l + (r-l)//2
            
            if arr[mid] < arr[mid+1]:
                l = mid+1
            elif arr[mid-1] > arr[mid]:
                r = mid-1
            else:
                return mid

        return -1
