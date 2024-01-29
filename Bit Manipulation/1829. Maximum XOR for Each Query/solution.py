class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        res = []
        n = len(nums)
        XOR = nums[0]
        for i in range(1, n):
            XOR ^= nums[i]

        bitmask = (1<<maximumBit)-1
        for i in range(n):
            if n-i < n:
                XOR ^= nums[n-i]
            suffix = XOR&bitmask
            k = bitmask^suffix
            res.append(k)

        return res
