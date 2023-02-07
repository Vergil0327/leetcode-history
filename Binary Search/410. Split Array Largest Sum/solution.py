class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def lessThan(upperbound):
            curr = 0
            cnt = 0
            for num in nums:
                if num > upperbound: return False
                if curr + num > upperbound:
                    curr = 0
                    cnt += 1
                curr += num

            if curr > 0:
                cnt += 1
            return cnt <= k

        l, r = 0, sum(nums)
        while l < r:
            mid = l + (r-l)//2
            if lessThan(mid):
                r = mid
            else:
                l = mid+1
        return l