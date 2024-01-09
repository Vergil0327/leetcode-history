class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        target2idx = {num: i for i, num in enumerate(target)}
        LIS = []
        for num in arr:
            if num in target2idx:
                tId = target2idx[num]
                j = bisect_left(LIS, tId)
                if j == len(LIS):
                    LIS.append(tId)
                else:
                    LIS[j] = tId
        return len(target) - len(LIS)
