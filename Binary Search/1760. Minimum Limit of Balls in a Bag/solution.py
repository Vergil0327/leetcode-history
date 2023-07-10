class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort(reverse=True)

        l, r = 1, max(nums)

        while l < r:
            mid = l + (r-l)//2
            if self.check(mid, maxOperations, nums):
                r = mid
            else:
                l = mid+1
        return l
    def check(self, mid, maxOps, nums):
        n = 0
        for num in nums:
            if num <= mid: break
            n += num//mid if num%mid!=0 else num//mid-1

        return n <= maxOps
