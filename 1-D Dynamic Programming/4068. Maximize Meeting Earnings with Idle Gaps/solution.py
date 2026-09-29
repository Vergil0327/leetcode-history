from bisect import bisect_right

"""
================================================================================
KEY INSIGHT & APPROACH
================================================================================

1. Algebraic Rearrangement of Idle Time:
   - For a sequence of non-overlapping meetings M_1, M_2, ..., M_k sorted by start times:
       Total Earnings = Sum(r_j) + Sum(s_{j+1} - e_j)
                      = (r_1 + r_2 + ... + r_k) + (s_2 - e_1 + s_3 - e_2 + ... + s_k - e_{k-1})
   - Regrouping terms by each meeting j:
       Total Earnings = -s(M_1) + Sum_{j=1..k} (r_j + s_j - e_j) + e(M_k)
   - Define weight w_j = r_j + s_j - e_j for each meeting j.
   - Total Earnings simplify to: -s_1 + w_1 + w_2 + ... + w_k + e_k.

2. Dynamic Programming State:
   - Sort all meetings by end times e_i.
   - Let DP[i] be the maximum prefix score (-s_1 + w_1 + ... + w_i) for a non-overlapping
     meeting sequence ending at meeting i:
       DP[i] = w_i + max( -s_i,  max_{e_j <= s_i} DP[j] )
   - Here, -s_i handles the case where meeting i is the FIRST meeting (k = 1), 
     while max_{e_j <= s_i} DP[j] extends a previously valid chain.

3. Optimization via Binary Search & Prefix Max:
   - Since meetings are sorted by end time `e_j`, we can find the largest index `j`
     such that `e_j <= s_i` in O(log N) time using binary search (`bisect_right`).
   - Maintain a running prefix maximum `pref_max[i] = max_{0 <= k <= i} DP[k]` so that
     `max_{e_j <= s_i} DP[j]` is queried in O(1) time after binary searching.
   - Total earnings if meeting i is the final meeting in the chosen set: DP[i] + e_i.

4. Complexity:
   - Time Complexity: O(N log N) due to sorting and N binary search lookups.
   - Space Complexity: O(N) for storing the DP and prefix maximum arrays.
================================================================================
"""
class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        # Sort meetings by end time
        meetings.sort(key=lambda x: x[1])
        
        ends = [m[1] for m in meetings]
        n = len(meetings)
        
        dp = [0] * n
        pref_max = [0] * n
        ans = 0
        
        for i in range(n):
            s, e, r = meetings[i]
            w = r + s - e
            
            # Find the last meeting that ends at or before start time s
            idx = bisect_right(ends, s) - 1
            
            if idx >= 0:
                best_prev = pref_max[idx]
            else:
                best_prev = float('-inf')
                
            dp[i] = w + max(-s, best_prev)
            
            # Maintain prefix maximum of DP array
            if i == 0:
                pref_max[i] = dp[i]
            else:
                pref_max[i] = max(pref_max[i - 1], dp[i])
                
            ans = max(ans, dp[i] + e)
            
        return ans