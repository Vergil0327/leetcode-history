class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        def count(dist):
            cnt = 0
            for i in range(n):
                j = bisect_right(nums, dist+nums[i])
                cnt += max(0, (j-1)-i)
            return cnt

        l, r = 0, nums[-1]-nums[0]
        while l < r:
            mid = l + (r-l)//2
            if count(mid) < k:
                l = mid+1
            else:
                r = mid
        return l