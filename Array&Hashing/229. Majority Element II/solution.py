class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []

        cnt1, cnt2 = 0, 0
        maj1, maj2 = -inf, -inf
        for num in nums:
            if num == maj1:
                cnt1 += 1
            elif num == maj2:
                cnt2 += 1
            elif cnt1 == 0:
                maj1 = num
                cnt1 = 1
            elif cnt2 == 0:
                maj2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        res = []
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == maj1:
                cnt1 += 1
            if num == maj2:
                cnt2 += 1

        if cnt1 > len(nums)//3:
            res.append(maj1)
        if maj2 != maj1 and cnt2 > len(nums)//3:
            res.append(maj2)
        return res
        
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [num for num, freq in counter.items() if freq > len(nums)//3]