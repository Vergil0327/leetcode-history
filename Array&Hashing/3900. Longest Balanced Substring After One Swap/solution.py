class Solution:
    """
    The Correct Swap Logic
    For a substring $s[i:j]$ of length $L$:
    1. Balance $0$: If it has $L/2$ zeros and $L/2$ ones, it is already balanced. No swap needed (or swap two identical characters).
    2. Balance $+2$ (e.g., three $1$s, one $0$): This can be fixed if there is at least one '0' outside the range $[i, j]$.
    3. Balance $-2$ (e.g., three $0$s, one $1$): This can be fixed if there is at least one '1' outside the range $[i, j]$.

    Why the Hash Map needs to be more clever
    We can't just store the first index. If the first index we stored results in a substring that uses all the zeros in the string, we can't swap a zero in from the outside. We need to check if:
    - zeros_in_substring < total_zeros (to swap a 0 in)
    - ones_in_substring < total_ones (to swap a 1 in)
    """
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        t1 = s.count('1')
        t0 = n - t1
        
        # We'll use a prefix sum for '1's (count1) and '0's (count0)
        c1 = [0] * (n + 1)
        c0 = [0] * (n + 1)
        for i in range(n):
            c1[i+1] = c1[i] + (1 if s[i] == '1' else 0)
            c0[i+1] = c0[i] + (1 if s[i] == '0' else 0)
            
        max_len = 0
        
        # O(N^2) is too slow for 10^5, so we use a Two-Pointer/Sliding Window 
        # approach or a modified hash map. Since length is what we maximize:
        
        # Let's iterate over all possible lengths L (must be even)
        # and check if any window of length L works. 
        # But even better: Since we want the longest, we can use the hash map 
        # but store multiple indices if needed. 
        # Actually, for a fixed balance offset, usually the earliest index is best.
        
        first_seen = {} # balance -> list of (index, zeros_count, ones_count)
        first_seen[0] = [(-1, 0, 0)]
        
        curr_bal = 0
        for i in range(n):
            curr_bal += 1 if s[i] == '1' else -1
            
            # Check for balance offsets
            for offset in [0, 2, -2]:
                target = curr_bal - offset
                if target in first_seen:
                    for prev_idx, prev_c0, prev_c1 in first_seen[target]:
                        win_c0 = c0[i+1] - prev_c0
                        win_c1 = c1[i+1] - prev_c1
                        
                        can_fix = False
                        if offset == 0: 
                            can_fix = True
                        elif offset == 2 and win_c1 > 0 and t0 > win_c0:
                            # Has extra 1s, and there's a 0 outside to swap in
                            can_fix = True
                        elif offset == -2 and win_c0 > 0 and t1 > win_c1:
                            # Has extra 0s, and there's a 1 outside to swap in
                            can_fix = True
                        
                        if can_fix:
                            max_len = max(max_len, i - prev_idx)
                            # Once we find a fix for this offset, the earliest index 
                            # is usually enough, but we might need to break or 
                            # optimize to avoid O(N^2)
                            break 
            
            if curr_bal not in first_seen:
                first_seen[curr_bal] = [(i, c0[i+1], c1[i+1])]
            else:
                # Optimization: Only keep the record if it has fewer 0s or 1s 
                # than existing records to keep the outside count high.
                # In practice, keeping the 2-3 earliest is enough.

                # The reason you cannot skip that optimization is that the earliest index for a specific balance is not always the best index when a swap is involved.
                # In a standard "Longest Substring" problem, the earliest index is always superior because it results in the longest window.
                # However, in this problem, the window must satisfy a secondary condition: there must be a character available outside the window to swap in.
                # The "All-In" Problem
                # Imagine a scenario where the very first time you see a balance of 0, it happens at an index where you have already used every single '0' in the string.
                # Earliest Index ($A$): Longest possible window, but uses all zeros. If we need to swap a zero in (balance $+2$), we can't, because t0 == win_c0.
                # Second Index ($B$): Slightly shorter window, but leaves one zero outside. If we need to swap a zero in, we can.If you only store the earliest index, you might find a window that is technically "long" but "invalid" because it's impossible to fix.
                if len(first_seen[curr_bal]) < 2:
                    first_seen[curr_bal].append((i, c0[i+1], c1[i+1]))
                    
        return max_len