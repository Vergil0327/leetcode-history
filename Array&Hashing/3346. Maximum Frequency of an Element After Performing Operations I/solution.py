class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        mn = min(nums)
        mx = max(nums)
        diff = defaultdict(int)
        for num in nums:
            diff[num-k] += 1
            diff[num+k+1] -= 1
        
        for i in range(mn-k, mx+k+1):
            diff[i] += diff[i-1]

        count = Counter(nums)
        res = 0
        for i in range(mn, mx+1):
            res = max(res, count[i] + min(numOperations, diff[i]-count[i]))
        return res
        
# - use difference array to know the maximum frequency in range [min(nums)-k, max(nums)+k]
# - iterate value in range of [min(nums), max(nums)] to find maximum possible frequency of valid value