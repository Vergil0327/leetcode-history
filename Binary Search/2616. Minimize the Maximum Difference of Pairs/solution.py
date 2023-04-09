class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        # greedily take pairs
        def check(mid):
            pairs = 0
            i = 0
            while i < n:
                if i+1 < n and nums[i+1]-nums[i] <= mid:
                    i = i+2
                    pairs += 1
                else:
                    i += 1
            return pairs >= p
        
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return l
        