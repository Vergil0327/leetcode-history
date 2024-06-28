class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [i-nums[i] for i in range(n)]

        count = Counter()
        res = 0
        for i in range(n):
            res += i - count[arr[i]]
            count[arr[i]] += 1
        return res
