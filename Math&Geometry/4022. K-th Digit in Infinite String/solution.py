class Solution:
    def kthDigit(self, k: int) -> int:
        # Base case: block b = 0 (numbers 1..9)
        if k <= 9:
            return k
        
        # Subtract the 9 digits of block b = 0
        k -= 9
        
        # d is the digit length of numbers inside block b
        # b = 1..9 has 1-digit b, so numbers in block b have d = 2 digits
        d = 2 
        while True:
            # Number of blocks b where b has (d-1) digits is 9 * 10**(d-2)
            blocks_cnt = 9 * (10 ** (d - 2))
            digits_in_group = blocks_cnt * 10 * d
            if k > digits_in_group:
                k -= digits_in_group
                d += 1
            else:
                break
        
        # Find the specific block b
        digits_per_block = 10 * d
        block_offset = (k - 1) // digits_per_block
        b = (10 ** (d - 2)) + block_offset
        
        # Position inside block b (0-indexed)
        k_in_block = (k - 1) % digits_per_block
        
        # Identify the exact integer and digit
        num_idx = k_in_block // d
        digit_idx = k_in_block % d
        
        # Determine target number based on parity of b
        if b % 2 == 0:
            target_num = 10 * b + num_idx
        else:
            target_num = 10 * b + 9 - num_idx
        
        return int(str(target_num)[digit_idx])