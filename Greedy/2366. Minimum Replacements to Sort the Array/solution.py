class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                n = nums[i]//nums[i+1]
                remain = nums[i]%nums[i+1]

                if remain == 0: # equally break up into n pieces of nums[i+1] => n-1 split
                    res += n-1
                    nums[i] = nums[i+1]
                else: # break up into 1 + n pieces => n split
                    some = (nums[i+1]-remain)//(n+1)
                    remain = remain + n*some
                    x = nums[i+1]-some

                    res += n
                    if remain == x:
                        nums[i] = remain
                    else:
                        nums[i] = x-1
        return res
