class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        n = len(nums)
        l = r = res = 0
        count = Counter()
        while r < n:
            count[nums[r]] += 1
            r += 1

            while l < r and len(count) >= distinct:
                res += n-r+1

                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1

        return res