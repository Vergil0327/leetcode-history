# Binary Search
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # edge case: [2,3,5] target: 11
        if sum(arr) < target: return max(arr)

        def calculate(threshold):
            total = 0
            for num in arr:
                total += min(num, threshold)
            return total

        l, r = 0, 100000
        while l < r:
            mid = r - (r-l)//2
            SUM = calculate(mid)
            if SUM < target:
                l = mid
            else:
                r = mid-1
        return l if abs(calculate(l)-target) <= abs(calculate(l+1)-target) else l+1

# PrefixSum + Binary Search
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # edge case: [2,3,5] target: 11
        if sum(arr) < target: return max(arr)

        n = len(arr)

        arr.sort()
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + arr[i-1]
        
        def quickCal(threshold):
            i = bisect.bisect_left(arr, threshold)
            return (n-i)*threshold + presum[i]

        l, r = 0, 100000
        while l < r:
            mid = r - (r-l)//2
            SUM = quickCal(mid)
            if SUM < target:
                l = mid
            else:
                r = mid-1
        return l if abs(quickCal(l)-target) <= abs(quickCal(l+1)-target) else l+1