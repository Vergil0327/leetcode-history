from sortedcontainers import SortedDict
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)

        arr = [nums[i]-i for i in range(n)]
        subseq = SortedDict()
        res = -inf

        for i in range(n):
            if nums[i] <= 0:
                res = max(res, nums[i])
            else:
                key = arr[i]

                _sum = nums[i]
                j = subseq.bisect_right(key)-1
                if j >= 0:
                    _sum = max(_sum, subseq.peekitem(j)[1]+_sum)

                while j+1 < len(subseq) and subseq.peekitem(j+1)[1] < _sum:
                    subseq.popitem(j+1)

                subseq[key] = _sum
                res = max(res, _sum)
        return res
                    
        
            
