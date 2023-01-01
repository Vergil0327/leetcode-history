# O(1) Space
# O(1) Space 解法很巧妙，由於一定存在眾數，而眾數的定義就是出現的頻率最多
# 因此當freq = 0時我們就假設他是眾數，遇到相同的數就頻率加一，反之則減一
# 由於眾數會是出現最多次的，因此最後留下的數即為眾數
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        freq = 0
        for num in nums:
            if freq == 0:
                maj = num
                freq = 1
            elif num == maj:
                freq += 1
            else:
                freq -= 1
        return maj

# O(n) Space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        cnt = -inf
        res = 0
        for num in nums:
            if counter[num] > cnt:
                cnt = counter[num]
                res = num
        return res