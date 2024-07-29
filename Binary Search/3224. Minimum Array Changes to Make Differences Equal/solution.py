class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)

        countX = defaultdict(int)
        change1Threshold = []
        for i in range(n//2):
            x = abs(nums[i] - nums[n-i-1])
            countX[x] += 1

            # let a < b
            a, b = min(nums[i], nums[n-i-1]), max(nums[i], nums[n-i-1])
            threshold = max(b, k-a)
            change1Threshold.append(threshold)

        change1Threshold.sort()

        res = n
        for x in countX.keys():
            invalid = n//2 - countX[x]
            cntChange2 = bisect_left(change1Threshold, x)

            res = min(res, invalid + cntChange2)
        return res