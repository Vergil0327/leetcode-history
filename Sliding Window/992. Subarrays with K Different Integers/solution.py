class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            n = len(nums)
            res = l = r = 0
            window = defaultdict(int)

            while r < n:
                window[nums[r]] += 1
                r += 1

                while l < r and len(window) > k:
                    window[nums[l]] -= 1
                    if window[nums[l]] == 0:
                        del window[nums[l]]
                    l += 1

                res += r-l-1
                    
            return res

        return atMost(k) - atMost(k-1)
