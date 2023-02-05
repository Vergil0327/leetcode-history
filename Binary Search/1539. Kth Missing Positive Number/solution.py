class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        l, r = 0, n
        while l < r:
            mid = l + (r-l)//2
            missing = arr[mid]-(mid+1)
            if missing < k:
                l = mid+1
            else:
                r = mid
        missing_used = l
        return missing_used+k
