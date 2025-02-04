class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def kadane(t):
            max_count = count = 0
            for num in nums:
                if num == t:
                    count += 1
                elif num == k:
                    count -= 1
                count = max(0, count)
                max_count = max(max_count, count)
            return max_count

        res = 0
        for target in range(1, 51):
            if target == k: continue
            res = max(res, kadane(target))
        return res + nums.count(k)
