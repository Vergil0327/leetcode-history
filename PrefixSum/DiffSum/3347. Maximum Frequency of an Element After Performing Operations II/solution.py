class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        occurrence = Counter(nums)
        diff = defaultdict(int)
        positions = set()
        for num in nums:
            diff[num-k] += 1
            diff[num+k+1] -= 1

            positions.add(num-k)
            positions.add(num)
            positions.add(num+k+1)

        res = freq = 0
        for num in sorted(positions):
            freq += diff[num]

            res = max(res, occurrence[num] + min(numOperations, freq-occurrence[num]))
        return res
