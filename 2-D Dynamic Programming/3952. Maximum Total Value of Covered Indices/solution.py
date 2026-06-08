from functools import cache
from typing import List

# DP
class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)
        
        # prev_covered: 
        # 0 -> index i-1 is NOT covered
        # 1 -> index i-1 IS covered
        @cache
        def solve(i: int, prev_covered: int) -> int:
            # Base Case: Processed all indices
            if i == n:
                # Boundary condition: Check if the last index (n-1) was left covered
                return nums[n-1] if prev_covered else 0
            
            # Find the value of the previous index (if it exists)
            val_prev = nums[i-1] if (i > 0 and prev_covered) else 0
            
            # Case 1: No token at index i
            if s[i] == '0':
                # Index i is forced to remain UNCOVERED (0).
                # We collect the value of i-1 right now if it was covered.
                return val_prev + solve(i + 1, 0)
            
            # Case 2: Token exists at index i
            else:
                # Choice A: Leave the token at index i
                # Index i becomes COVERED (1) for the next step.
                # We collect the value of i-1 right now if it was covered.
                stay_choice = val_prev + solve(i + 1, 1)
                
                # Choice B: Move the token to index i-1
                # This is ONLY allowed if index i-1 was NOT already covered.
                move_choice = float('-inf')
                if i > 0 and not prev_covered:
                    # By moving the token, index i-1 becomes COVERED (we collect its value),
                    # but index i is left completely UNCOVERED (0) for the next step.
                    move_choice = nums[i-1] + solve(i + 1, 0)
                    
                return max(stay_choice, move_choice)
                
        # Start at index 0. Before index 0, there is no index -1, so it cannot be covered (0).
        return solve(0, 0)