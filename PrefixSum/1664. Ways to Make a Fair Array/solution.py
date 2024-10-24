class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd = [0]*(n+1)
        even = [0]*(n+1)
        for i in range(n):
            even[i+1] = even[i]
            odd[i+1] = odd[i]
            if i%2 == 0:
                even[i+1] += nums[i]
            else:
                odd[i+1] += nums[i]

        res = 0
        for i in range(n):
            suf_evn = even[n] - even[i+1]
            suf_odd = odd[n] - odd[i+1]
            
            res += int(odd[i] + suf_evn == even[i] + suf_odd)
        return res
