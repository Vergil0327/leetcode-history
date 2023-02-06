class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            total = 0
            for num in nums:
                total += ceil(num/divisor)
            return total

        l, r = 1, max(nums)
        while l < r:
            mid = l + (r-l)//2
            SUM = check(mid)
            if SUM > threshold:
                l = mid+1
            else:
                r = mid
                
        return l