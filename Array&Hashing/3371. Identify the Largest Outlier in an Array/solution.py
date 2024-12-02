class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        nums.sort()
        res = -inf
        count = Counter(nums)
        for i, out in enumerate(nums):
            total_special2 = total - out
            if total_special2%2 == 0:
                special_sum = total_special2 // 2 
                
                if out == special_sum:
                    if count[special_sum] > 1:
                        res = max(res, out)
                else:
                    if count[special_sum] > 0:
                        res = max(res, out)
        return res
