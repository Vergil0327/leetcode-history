"""
### Problem Breakdown & Mathematical Logic

We need to determine if B = b * y is a substring of A = a * x.
Let:
    |A| = len(a) * x
    |B| = len(b) * y

1. Length Pre-Check:
   If |B| > |A|, a longer string can never be a substring of a shorter string, 
   so we immediately return False.

2. Periodic Alignment to an Offset i in [0, len(a) - 1]:
   - The string A = a * x is a prefix of the infinite periodic string a^∞.
   - If B appears anywhere in A at starting index `pos >= 0`, then B must match 
     a^∞[pos ... pos + |B| - 1].
   - Because a^∞ has period |a|, the infinite sequence starting at `pos` is 
     identical to the infinite sequence starting at `i = pos % len(a)`.
   - Moreover, since i <= pos, if the occurrence at `pos` fits inside A 
     (pos + |B| <= |A|), then the occurrence at `i` also fits inside A 
     (i + |B| <= pos + |B| <= |A|).
   - Therefore, B appears in A if and only if there is SOME offset i in [0, len(a) - 1] 
     such that:
         1. i + |B| <= |A|
         2. B matches a^∞[i ... i + |B| - 1]

3. Fine and Wilf's Periodicity Lemma (O(1) Verification):
   - Notice |B| can be up to 100 * 10^9 = 10^11, so we cannot verify all characters of B directly.
   - However, B has period p = len(b), and a^∞[i...] has period q = len(a).
   - By Fine and Wilf's Theorem (1965), if two periodic words with periods p and q 
     agree on a prefix of length:
         L = p + q - gcd(p, q)
     then they must agree everywhere for all subsequent characters!
   - Therefore, we only need to compare at most:
         check_len = min(|B|, len(a) + len(b) - gcd(len(a), len(b)))
     characters!
   - Since len(a), len(b) <= 100:
         check_len <= 100 + 100 - 1 = 199
   - For each offset i, comparing at most 199 characters guarantees whether 
     the entire B = b * y of length 10^11 matches!

=== Complexity Analysis ===

1. Time Complexity: O(|a| * (|a| + |b|))
   - gcd(len(a), len(b)) takes O(log(min(|a|, |b|))) time.
   - Outer loop tests at most |a| <= 100 starting positions i.
   - Inner loop runs at most check_len <= |a| + |b| - 1 <= 199 steps.
   - Total operations: at most 100 * 199 ≈ 20,000 character comparisons.
   - Total Time Complexity: O(|a| * (|a| + |b|)) ≈ 0.003 seconds, regardless of 
     how large x and y are (even up to 10^9).

2. Space Complexity: O(1)
   - Only a few integer variables are stored.
   - Total Auxiliary Space: O(1).
"""
import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
        len_a = len(a)
        len_b = len(b)
        total_a = len_a * x
        total_b = len_b * y
        
        # Substring cannot be longer than the source string
        if total_b > total_a:
            return False
        
        # Bound derived from Fine and Wilf's Periodicity Theorem
        bound = len_a + len_b - math.gcd(len_a, len_b)
        check_len = min(total_b, bound)
        
        # Try all possible starting offsets i in [0, len_a - 1]
        for i in range(len_a):
            # The substring starting at offset i must fit within a * x
            if i + total_b > total_a:
                continue
            
            # Check if B matches a^∞[i...] for check_len characters
            match = True
            for j in range(check_len):
                if b[j % len_b] != a[(i + j) % len_a]:
                    match = False
                    break
            
            if match:
                return True
                
        return False