class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        n = len(nums)
        
        xor = 0
        for i in range(n):
            xor ^= nums[i]
        
        # Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.
        if xor == 0: return True

        return len(nums)%2 == 0
