from functools import cmp_to_key

"""
The core idea is a Greedy Ratio Sort. To maximize a binary number, you must ensure that '1's are as far to the left (higher significance) as possible.

1. The Conflict
Every time you place a segment, its total length (ones + zeros) "pushes" all subsequent ones to the right, reducing their value.

- A segment with many ones is a high-value prize.
- A segment with many zeros is a high-cost penalty (it shifts everything else to the right).

2. The Concatenation Rule
If you have two segments, $A$ and $B$, you simply compare which order is better: is $AB > BA$?

- In $AB$, segment $A$ is at the top, and segment $B$ is shifted by $A$'s length.
- In $BA$, segment $B$ is at the top, and segment $A$ is shifted by $B$'s length.

3. Why simple sorting fails
You cannot just sort by "most ones" because a segment with $10,000$ ones but $50,000$ zeros is actually a "bad" segment—it has a massive "cost" that outweighs its "value."

The math $V_A(2^{L_B} - 1) > V_B(2^{L_A} - 1)$ creates a priority ratio. We use cross-multiplication in the code because it allows us to compare these ratios using exact integers, avoiding the precision errors that happen when dividing large powers of 2.

4. Summary
We order the segments such that those with the best "value-to-shift" ratio come first. This ensures that the most significant bits are filled with '1's while minimizing the distance that the remaining '1's are pushed into lower-value positions.
"""
class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        mod = 1000000007
        n = len(nums1)
        
        # We need to sort segments (a, b) such that concatenating A then B
        # results in a larger value than B then A.
        # Val(A) = (2^nums1_A - 1) * 2^nums0_A
        # Length(A) = nums1_A + nums0_A
        # AB > BA  =>  Val(A) * 2^Length(B) + Val(B) > Val(B) * 2^Length(A) + Val(A)
        
        def compare(idx1, idx2):
            # cross-multiplication of:
            # (2^n1_1 - 1) * 2^n0_1 * (2^(n1_2 + n0_2) - 1) 
            # vs 
            # (2^n1_2 - 1) * 2^n0_2 * (2^(n1_1 + n0_1) - 1)
            
            # Using bit shifts (<<) is much faster than pow() for large integers
            a_ones, a_zeros = nums1[idx1], nums0[idx1]
            b_ones, b_zeros = nums1[idx2], nums0[idx2]
            
            # Left side: Val(A) * (2^Len(B) - 1)
            left = ((1 << a_ones) - 1) << a_zeros
            left *= ((1 << (b_ones + b_zeros)) - 1)
            
            # Right side: Val(B) * (2^Len(A) - 1)
            right = ((1 << b_ones) - 1) << b_zeros
            right *= ((1 << (a_ones + a_zeros)) - 1)
            
            if left > right:
                return -1
            if left < right:
                return 1
            return 0

        # Sort indices based on the cross-multiplication comparison
        indices = list(range(n))
        indices.sort(key=cmp_to_key(compare))
        
        res = 0
        # Start from the far left (highest power of 2)
        # The total number of bits determines the initial shift
        current_shift = sum(nums1) + sum(nums0)
        
        for idx in indices:
            o, z = nums1[idx], nums0[idx]
            if o > 0:
                # Value of 'o' ones: (2^o - 1)
                # This block of ones is shifted left by (current_shift - o)
                # because the 'z' zeros of this segment are to its right.
                
                term = (pow(2, o, mod) - 1) * pow(2, current_shift - o, mod)
                res = (res + term) % mod
            
            # Move the cursor to the right by the total length of this segment
            current_shift -= (o + z)
            
        return res % mod