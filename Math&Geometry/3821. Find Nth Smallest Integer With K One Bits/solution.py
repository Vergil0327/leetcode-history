"""
The Efficient Strategy:

Greedy ConstructionInstead of counting every number, we "jump" through the bit positions using combinations.
We want to find the smallest number $X$ such that there are at least $n$ numbers $\le X$ with exactly $k$ set bits.1. 

1. Precompute Binomial Coefficients

We need to know how many ways we can choose $r$ bits out of $m$ positions.
This is $C(m, r)$ or $\binom{m}{r}$.$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$2.

2. Bit-by-Bit Decision

We iterate from the highest possible bit (49 down to 0).

    1. For each bit $i$:If we set the $i$-th bit to 1, how many numbers with $k$ bits exist that are smaller than this?This is simply $\binom{i}{k}$.
    2. If $n$ is greater than $\binom{i}{k}$, it means our target number must have the $i$-th bit set.
    3. We subtract $\binom{i}{k}$ from $n$ and move to the next bit, looking for the remaining $k-1$ bits.
    4. If $n$ is less than or equal to $\binom{i}{k}$, we keep the $i$-th bit as 0 and look for $k$ bits in the remaining lower positions.
"""


from math import comb

class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        res = 0
        remaining_k = k
        
        # Iterate from MSB (bit 49) down to 0
        for i in range(49, -1, -1):
            if remaining_k == 0:
                break
            
            # Count how many numbers have exactly 'remaining_k' bits 
            # in the remaining 'i' positions (from bit i-1 down to 0)
            count_with_bit_zero = comb(i, remaining_k)
            
            if n > count_with_bit_zero:
                # If n is larger than the combinations where this bit is 0,
                # then this bit MUST be 1.
                res |= (1 << i)
                n -= count_with_bit_zero
                remaining_k -= 1
            else:
                # Otherwise, the bit is 0, and we keep looking in smaller bits
                pass
                
        return res