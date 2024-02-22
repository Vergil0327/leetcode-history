class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:        
        nums.sort()
        
        x = numsDivide[0]
        for j in range(1, len(numsDivide)):
            x = gcd(x, numsDivide[j])

        for i, num in enumerate(nums):
            if x%num == 0: return i
        return -1
