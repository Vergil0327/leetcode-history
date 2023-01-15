class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)

        l, r, currPair = 0, 0, 0
        res = 0
        counter = defaultdict(int)

        while r < n: # [l, r), r exclusive
            num = nums[r]
            r += 1
            currPair += counter[num]
            counter[num] += 1
            
            while l < r and currPair >= k:
                res += n - (r-1)
                counter[nums[l]] -= 1
                currPair -= counter[nums[l]]
                l += 1
        return res
