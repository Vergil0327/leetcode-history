class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd = even = 0
        for num in nums:
            odd, even = max(odd, even-num), max(even, odd+num)
        return even