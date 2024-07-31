class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        sign = lambda x: int(x > 0) - int(x < 0)

        res = i = 0
        while i < n:
            start = target[i]-nums[i]
            if start == 0:
                i += 1
                continue

            if (curSign := sign(start)) > 0: # dec step
                curStep = 0
                j = i
                while j < n and sign(target[j]-nums[j]) == curSign:
                    diff = target[j] - nums[j]
                    if diff > curStep:
                        res += diff-curStep
                    curStep = diff
                    j += 1
                i = j
            else: # inc step
                curStep = 0
                j = i
                while j < n and sign(target[j]-nums[j]) == curSign:
                    diff = abs(target[j]-nums[j])
                    if diff > curStep:
                        res += diff - curStep
                    curStep = diff
                    j += 1
                i = j
        return res
