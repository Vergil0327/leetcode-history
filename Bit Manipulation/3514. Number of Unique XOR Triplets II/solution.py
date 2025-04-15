class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return n

        res = set()
        pairs = set()
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                pairs.add(nums[i]^nums[j])

            for p in pairs:
                res.add(p^nums[i])

        return len(res)
    