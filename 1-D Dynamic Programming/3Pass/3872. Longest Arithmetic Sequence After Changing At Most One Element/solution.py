class Solution:
    """
    The Logic
    We want to find the longest arithmetic subarray if we change nums[i]. There are three ways nums[i] can contribute to the maximum length:

    1. Extension: nums[i] is at the very beginning or end of a sequence (Length = Existing sequence + 1).

    2. Bridge: nums[i] is changed to perfectly connect a sequence on its left and a sequence on its right.

    3. No Change: The longest sequence already exists without changing anything.

    Step 1: Precompute Subarray Lengths
    We calculate two arrays:
    - L[i]: Length of the longest arithmetic subarray ending at index $i$.
    - R[i]: Length of the longest arithmetic subarray starting at index $i$.
    
    To calculate these, we check if the difference $nums[i] - nums[i-1]$ is the same as the previous difference.

    Step 2: Bridge Logic

    For every index $i$, if we change nums[i], can we connect nums[i-1] and nums[i+1]?
    This is only possible if the distance between them is even: $(nums[i+1] - nums[i-1]) \pmod 2 == 0$.

    The common difference would be $d = (nums[i+1] - nums[i-1]) // 2$.

    If the sequence ending at $i-1$ has difference $d$, and the sequence starting at $i+1$ also has difference $d$, then the new length is:
    $$L[i-1] + 1 + R[i+1]$$
    """
    def longestArithmetic(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3: return n
        
        # L[i] stores (difference, length) of arithmetic subarray ending at i
        L = [(0, 1)] * n
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            if i > 1 and diff == L[i-1][0]:
                L[i] = (diff, L[i-1][1] + 1)
            else:
                L[i] = (diff, 2)
        
        # R[i] stores (difference, length) of arithmetic subarray starting at i
        R = [(0, 1)] * n
        for i in range(n-2, -1, -1):
            diff = nums[i+1] - nums[i]
            if i < n-2 and diff == R[i+1][0]:
                R[i] = (diff, R[i+1][1] + 1)
            else:
                R[i] = (diff, 2)
        
        # Base result: any existing subarray + 1 (for the at most one change)
        ans = 0
        for i in range(n):
            ans = max(ans, L[i][1] + (1 if i < n-1 else 0))
            ans = max(ans, R[i][1] + (1 if i > 0 else 0))

        # Check bridging at each index i
        for i in range(1, n-1):
            # Try to bridge nums[i-1] and nums[i+1]
            total_diff = nums[i+1] - nums[i-1]
            if total_diff % 2 == 0:
                d = total_diff // 2
                current_len = 1 # The changed nums[i]
                
                # If left side matches the bridge difference
                if L[i-1][0] == d:
                    current_len += L[i-1][1]
                else:
                    current_len += 1 # Just nums[i-1]
                
                # If right side matches the bridge difference
                if R[i+1][0] == d:
                    current_len += R[i+1][1]
                else:
                    current_len += 1 # Just nums[i+1]
                
                ans = max(ans, current_len)
            
            # Special case: bridge with different logic
            # Even if total_diff isn't even, we could have [..., i-1] and [i+1, ...] 
            # where changing i only connects to one side. (Already handled by ans initialization)

        return min(ans, n)