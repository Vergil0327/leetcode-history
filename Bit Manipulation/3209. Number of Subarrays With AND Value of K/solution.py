class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        MAP = defaultdict(int)
        for i, num in enumerate(nums):
            nxt = defaultdict(int)
            for subarr, freq in MAP.items():
                bit = subarr&num
                nxt[bit] += freq

            nxt[num] += 1
            MAP = nxt
            res += MAP[k]
        return res
