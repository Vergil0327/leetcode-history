# we can easily brute force in O(n^2)
# but there is O(n) solution
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1]*(n-k+1)
        for i in range(n-k+1):
            if nums[i:i+k] == list(range(nums[i], nums[i]+k)):
                res[i] = nums[i]+k-1
        return res

