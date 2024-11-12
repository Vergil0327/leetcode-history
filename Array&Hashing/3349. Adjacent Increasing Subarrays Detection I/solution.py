class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        max_length = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                max_length[i] = max_length[i + 1] + 1
        
        for i in range(n - 2 * k + 1):
            if max_length[i] >= k and max_length[i + k] >= k:
                return True
        return False
    
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        max_length = [0] * (n+1)
        for i in range(n):
            if nums[i] > nums[i-1]:
                max_length[i+1] = max_length[i] + 1
            else:
                max_length[i+1] = 1


        for length in max_length:
            if length >= 2*k: return True

        for i in range(1, n+1):
            if i-k < 0: continue
            if max_length[i] >=k and max_length[i-k] >= k:
                return True
        return False