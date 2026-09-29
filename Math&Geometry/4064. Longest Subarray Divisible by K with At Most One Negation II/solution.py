"""
================================================================================
KEY INSIGHT & APPROACH
================================================================================

1. Mathematical Problem Formulation:
   - Without negation, subarray sum S(i, j) = (P[j+1] - P[i]) mod k.
   - Negating nums[m] (where i <= m <= j) changes sum by delta d_m = (2 * nums[m]) mod k.
   - Subarray sum becomes 0 mod k if:
       P[i] == (P[j+1] - d_m) mod k  <==>  P[j+1] == (P[i] + d_m) mod k

2. Bottleneck of Naive Iteration:
   - Scanning through all previously seen deltas at each right endpoint j takes O(N * K) time.
   - In Python, running ~3,000 iterations inside a loop of 100,000 elements causes TLE.

3. Key Optimization (Incremental Amortized Pairing):
   - Maintain `first_pos[r]`: earliest index where prefix remainder `r` appears.
   - Maintain `best_i[R]`: smallest valid left index `i` yielding target remainder `R`
     using exactly one element negation.
   - Validity Condition: Delta d_m at index m can ONLY pair with prefix remainder r if 
     `first_pos[r] <= m` (the start index must precede or equal the negated element).
   - Incremental Update: When encountering delta d_m at index m, pair d_m ONLY with 
     the newly discovered prefix remainders in `seen_P` not yet processed for d_m.
   - Result: Each unique pair (prefix remainder r, delta d) is combined AT MOST ONCE
     globally across the entire array traversal.

4. Time & Space Complexity:
   - Time Complexity: O(N + U_P * U_d), where U_P, U_d <= k are the counts of unique 
     prefix remainders and unique deltas. Total global updates are bounded by O(K^2).
   - Space Complexity: O(K) for direct array lookup tables.
================================================================================
"""
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # first_pos[r] = earliest index where prefix sum mod k == r
        # P[0] = 0 occurs at index 0
        first_pos = [float('inf')] * k
        first_pos[0] = 0
        
        # best_i[R] = smallest valid left index i to achieve target remainder R with 1 negation
        best_i = [float('inf')] * k
        
        # Maintain order of unique prefix remainders seen so far
        seen_P = [0]
        
        # Tracks how many prefix remainders in seen_P have been paired with each delta d
        last_processed_P_count = [0] * k
        
        max_len = 0
        P = 0
        
        for j, num in enumerate(nums):
            # 1. Update prefix sum and delta for current element
            P = (P + num) % k
            d = (2 * num) % k
            if d < 0:
                d += k
            
            # 2. Pair current delta d with all NEW prefix remainders in seen_P
            # Each (r, d) pair is processed AT MOST ONCE across the entire run
            start_idx = last_processed_P_count[d]
            curr_p_len = len(seen_P)
            
            if start_idx < curr_p_len:
                for idx in range(start_idx, curr_p_len):
                    r = seen_P[idx]
                    fp_r = first_pos[r]
                    R = (r + d) % k
                    if fp_r < best_i[R]:
                        best_i[R] = fp_r
                last_processed_P_count[d] = curr_p_len
            
            # 3. Check max length ending at index j
            # Case 1: No negation needed
            fp1 = first_pos[P]
            if fp1 <= j:
                max_len = max(max_len, j + 1 - fp1)
            
            # Case 2: Exactly 1 negation
            fp2 = best_i[P]
            if fp2 <= j:
                max_len = max(max_len, j + 1 - fp2)
            
            # 4. Record new prefix sum remainder if seen for the first time
            if first_pos[P] == float('inf'):
                first_pos[P] = j + 1
                seen_P.append(P)
                
        return max_len