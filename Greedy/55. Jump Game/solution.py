"""
仔細觀察可發現每個inde+nums[i]即為每個位置能抵達的最遠距離
因此只要遍歷過一遍確認有沒有辦法持續往前跳至終點即可

如果途中所能抵達的最遠距離是原地踏步, 並且尚未抵達終點, 那就返回False

注意edge case, nums = [0]時, 已經抵達終點
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farReach = nums[0]
        for i in range(n):
            farReach = max(farReach, i+nums[i])
            if i != n-1 and farReach == i: return False
        return farReach >= n-1