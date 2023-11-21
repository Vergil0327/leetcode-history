class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            rev = int(str(num)[::-1])
            arr.append(num-rev)

        count = defaultdict(int)
        res = 0
        for num in arr:
            res = (res + count[num]) % 1_000_000_007
            count[num] += 1
        return res
