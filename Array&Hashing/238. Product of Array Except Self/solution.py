class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for num in nums:
            pre.append(pre[-1]*num)

        n = len(nums)
        suf = [1]*(n+1)
        for i in range(n-1, -1, -1):
            suf[i] = suf[i+1]*nums[i]

        return [pre[i]*suf[i+1] for i in range(n)]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = []
        for num in nums:
            res.append(pre)
            pre *= num

        suf = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suf
            suf *= nums[i]
        return res
