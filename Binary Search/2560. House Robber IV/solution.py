class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(cap):
            takePrev = False
            cnt = 0
            for num in nums:
                if takePrev:
                    takePrev = False
                    continue
                if num <= cap:
                    cnt += 1
                    takePrev = True
            return cnt >= k

        l, r = min(nums), max(nums)
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l