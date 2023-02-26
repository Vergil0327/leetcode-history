class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def check(targetNumPair):
            pairs = 0
            j = n-1
            for i in range(j-targetNumPair, -1, -1):
                if nums[i] * 2 <= nums[j]:
                    j -= 1
                    pairs += 1
            return pairs >= targetNumPair

        l, r = 0, n//2
        while l < r:
            mid = r - (r-l)//2
            if check(mid):
                l = mid
            else:
                r = mid-1
        return l*2
    

class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        l, r = n//2-1, n-1
        ops = 0
        for i in range(l, -1, -1):
            if nums[i] * 2 <= nums[r]:
                r -= 1
                ops += 2
        return ops