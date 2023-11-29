class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            sarr = set([nums[i]])
            imb = 0
            for j in range(i+1, n):
                if nums[j] not in sarr:
                    if nums[j]-1 in sarr and nums[j]+1 in sarr:
                        imb -= 1
                    elif nums[j]-1 in sarr or nums[j]+1 in sarr:
                        pass
                    else:
                        imb += 1
                    sarr.add(nums[j])
                res += imb

        return res
