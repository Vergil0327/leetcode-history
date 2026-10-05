"""
### Plain Text Explanation for Fast Doubling

1. Core Concept:
   Instead of computing Fibonacci numbers sequentially (F_0, F_1, F_2, ... F_n) in O(n) time, 
   Fast Doubling jumps directly from F_k to F_2k in O(1) step.

2. Identities:
   Given two consecutive Fibonacci numbers (F_k, F_k+1):
   - F_2k   = F_k * (2 * F_{k+1} - F_k)
   - F_{2k+1} = F_k^2 + F_{k+1}^2

3. Step-by-Step Execution for n = 6 (binary '110'):
   - Start with k = 0: (F_0, F_1) = (0, 1)
   
   - Bit 1 (k = 1):
     Double (0, 1) -> F_0 = 0, F_1 = 1
     Since bit is 1, shift -> (F_1, F_2) = (1, 1)
     
   - Bit 2 (k = 3):
     Double (1, 1) -> F_2 = 1, F_3 = 2
     Since bit is 1, shift -> (F_3, F_4) = (2, 3)
     
   - Bit 3 (k = 6):
     Double (2, 3) -> F_6 = 2*(2*3 - 2) = 8, F_7 = 2^2 + 3^2 = 13
     Since bit is 0, keep -> (F_6, F_7) = (8, 13)

   Result: F_6 = 8.

4. Performance Comparison:
   - Linear Iteration: O(n) operations
   - Matrix Exponentiation: O(log n) time, requires 8 multiplications per step
   - Fast Doubling: O(log n) time, requires only 2 multiplications per step
"""

"""
Complexity Analysis
Time Complexity: $O(\log n)$ — Uses bitwise operations and fast-doubling to calculate $F_n$ in logarithmic time.
Space Complexity: $O(\log n)$ recursion stack (or $O(1)$ if using iterative matrix multiplication).

### Mathematical Approach & Proof

1. Characterization of Good Strings:
   A string is good if and only if every contiguous run of identical characters has an odd length.

2. Reduction to Odd Compositions:
   Any valid string of length n corresponds to a sequence of positive odd integers (L_1, L_2, ..., L_k) such that L_1 + L_2 + ... + L_k = n.

3. Recurrence for Odd Compositions f(n):
   Let f(n) be the number of ways to write n as an ordered sum of positive odd integers:
   - Base cases:
     f(1) = 1  ( composition: [1] )
     f(2) = 1  ( composition: [1, 1] )
   - For n >= 3:
     The last element in the sum can be 1, 3, 5, ...
     f(n) = f(n-1) + f(n-3) + f(n-5) + ...
     Substituting f(n-1) = f(n-2) + f(n-4) + f(n-6) + ... gives:
     f(n) = f(n-1) + f(n-2)
   
   Thus, f(n) = F_n (the n-th Fibonacci number, where F_1 = 1, F_2 = 1, F_3 = 2, ...).

4. Accounting for Starting Character:
   Once the sequence of run lengths is chosen, the characters alternate strictly (e.g., 'a'...'b'...'a'...).
   There are 2 choices for the initial character ('a' or 'b').
   
   Total Answer = 2 * F_n (mod 10^9 + 7)

5. Fast Computation for n <= 10^15:
   Compute F_n in O(log n) time using Fast Doubling Fibonacci or 2x2 Matrix Exponentiation.
"""
class Solution:
    def countGoodStrings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Fast Doubling method to calculate Fibonacci number F_n
        # Returns (F_n, F_{n+1})
        def fib(k: int) -> tuple[int, int]:
            if k == 0: return (0, 1)

            # Divide problem size in half
            a, b = fib(k >> 1)
            c = (a * ((2 * b - a) % MOD)) % MOD
            d = (a * a + b * b) % MOD

            # If current bit is 1, adjust from (F_2k, F_2k+1) to (F_2k+1, F_2k+2)
            if k & 1:
                return (d, (c + d) % MOD)
            else:
                return (c, d)
        
        # Total good strings = 2 * F_n % MOD
        fn, _ = fib(n)
        return (2 * fn) % MOD
