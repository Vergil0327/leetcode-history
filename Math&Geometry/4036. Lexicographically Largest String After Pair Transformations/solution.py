"""
Correct Approach
For each $x$:
- Calculate how many 'z' characters we need: z_count = x // (1 << 25).
- Take the remainder rem = x % (1 << 25).
- Convert rem into binary. For each set bit $k$ ($24$ down to $0$), append the corresponding character chr(ord('a') + k).
"""
class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        res = []
        Z_VAL = 1 << 25  # 2^25 corresponding to 'z'
        
        for x in nums:
            chars = []
            
            # 1. Take as many 'z's as possible
            z_count = x // Z_VAL
            if z_count > 0:
                chars.append('z' * z_count)
            
            # 2. Process the remaining value using binary representation
            rem = x % Z_VAL
            for k in range(24, -1, -1):
                if (rem >> k) & 1:
                    chars.append(chr(ord('a') + k))
                    
            res.append("".join(chars))
            
        return res