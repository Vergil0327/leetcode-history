class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n-2, -1, -1):
            while nums[i] > nums[i+1]:
                v = nums[i]
                for y in range(2, int(sqrt(v))+1):
                    if v%y == 0:
                        v = y
                        break
                if v == nums[i]: return -1
                nums[i] = v
                res += 1
                
        return res