"""
Algorithm Approach & Mathematical Insights:

1. Operations Preserve Parity:
   - Each operation changes x by +2 or -2, which keeps the parity (even or odd) of x UNCHANGED.
   - Therefore, an even number can ONLY be transformed into an EVEN positive palindrome, and an odd number can ONLY be transformed into an ODD positive palindrome.
   - The cost to change x into a palindrome p of the same parity is |x - p| // 2 operations.

2. Precomputing Candidates:
   - Since nums[i] <= 10^9, target palindromes can range up to ~10^9 + extra buffer.
   - Generating palindromes up to 2 * 10^9 can be done by generating half-prefixes (from 1 up to ~10^5) and mirroring them:
     * Odd length palindrome: prefix + reverse(prefix[:-1])
     * Even length palindrome: prefix + reverse(prefix)
   - Filter all valid palindromes > 0 and divide them into two sorted lists:
     * even_palindromes: [2, 4, 6, 8, 22, 44, 66, 88, 202, ...]
     * odd_palindromes:  [1, 3, 5, 7, 9, 11, 33, 55, 77, 99, 101, ...]

3. Independent Element Lookup via Binary Search:
   - Each element in nums is completely independent.
   - For each x in nums:
     * Select target list based on x % 2.
     * Use binary search (bisect_left) to find the closest palindromes <= x and >= x.
     * The minimum operations for x is min(|x - p| // 2) over the closest palindromes.
   - Total answer is the sum of minimum operations across all elements.

Complexity Analysis:
- Precomputation Time: O(M log M) where M ≈ 2 * 10^5 palindromes generated once globally (takes ~20ms).
- Query Time: O(N log M) per testcase, where N <= 10^5 and log M ≈ 18 comparisons per element. Overall time < 0.1s.
- Space Complexity: O(M) ≈ 200,000 numbers in memory across all testcases.
"""


from bisect import bisect_left

# Global precomputation of palindromes separated by parity
EVEN_PALINDROMES = []
ODD_PALINDROMES = []

def _precompute():
    palindromes = set()
    
    # Generate palindromes by mirroring prefixes up to 5 digits (covers up to ~2 * 10^9)
    for i in range(1, 100000):
        s = str(i)
        rev = s[::-1]
        
        # Odd-length palindrome
        p1 = int(s + rev[1:])
        if p1 > 0:
            palindromes.add(p1)
            
        # Even-length palindrome
        p2 = int(s + rev)
        if p2 > 0:
            palindromes.add(p2)
            
    sorted_p = sorted(palindromes)
    for p in sorted_p:
        if p % 2 == 0:
            EVEN_PALINDROMES.append(p)
        else:
            ODD_PALINDROMES.append(p)

_precompute()


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        total_ops = 0
        
        for x in nums:
            p_list = EVEN_PALINDROMES if x % 2 == 0 else ODD_PALINDROMES
            
            idx = bisect_left(p_list, x)
            min_ops = float('inf')
            
            # Check candidate at or right of x
            if idx < len(p_list):
                min_ops = min(min_ops, (p_list[idx] - x) // 2)
                
            # Check candidate left of x
            if idx > 0:
                min_ops = min(min_ops, (x - p_list[idx - 1]) // 2)
                
            total_ops += min_ops
            
        return total_ops
