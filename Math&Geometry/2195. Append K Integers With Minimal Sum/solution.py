class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = [0] + list(set(nums))
        nums.sort()
        nums = nums + [nums[-1]+k+1]
        n = len(nums)

        res = 0
        for i in range(n-1):
            if nums[i] == nums[i+1]: continue

            start, end = nums[i]+1, nums[i+1]-1
            m = end-start+1

            if k >= m:
                k -= m
                res += (start+end)*m//2
            else:
                end = start+k-1
                res += (start+end)*k//2
                k = 0
            if k == 0: break

        return res
