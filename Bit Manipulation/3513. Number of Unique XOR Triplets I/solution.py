class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # range [1,n]
        n = len(nums)
        if n < 3: return n

        return pow(2, n.bit_length())
