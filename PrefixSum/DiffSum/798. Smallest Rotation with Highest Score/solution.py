class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)

        diff = [0] * n
        for i in range(n):
            if nums[i] <= i:
                diff[0] += 1
                diff[(i-nums[i]+1)%n] -= 1
                diff[(i+1)%n] += 1
            else:
                diff[(i+1)%n] += 1
                diff[(i-nums[i]+n+1)%n] -= 1

        res = maxScore = score = 0
        for k in range(n):
            score += diff[k]
            if score > maxScore:
                maxScore = score
                res = k
        return res
