from functools import lru_cache

class Solution:
    """
    1. Identify the Path Indices
    
    The 16-digit string is formed by placing digits in row-major order.
        - Row $i$, Column $j$ corresponds to the index $(i \times 4 + j)$ in the 16-digit string.
        - Starting at $(0,0)$, we follow the directions to find exactly 7 indices.
    These indices will always be strictly increasing because we only move Down or Right.

    2. Digit DP Strategy
    
    We define a function $f(N)$ that counts the number of "good" integers in the range $[0, N]$. The final answer is $f(r) - f(l-1)$.

    dp(pos, is_tight, path_idx_count, last_path_digit)
    - pos: The current digit position being filled (0 to 15).
    - is_tight: Boolean flag indicating if we are restricted by the digits of $N$.
    - last_path_digit: The value of the previous digit visited on the path (used to ensure the non-decreasing property).
    """
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        # Determine the 7 indices visited on the 4x4 grid
        path_indices = [0] # Starting at (0, 0) -> index 0
        r_coord, c_coord = 0, 0
        for move in directions:
            if move == 'D':
                r_coord += 1
            else:
                c_coord += 1
            path_indices.append(r_coord * 4 + c_coord)
        
        # Convert path_indices to a set for O(1) lookup during DP
        path_set = set(path_indices)
        

        def count_upto(n_str: str) -> int:
            # Ensure the number string is exactly 16 digits for row-major mapping
            n_str = n_str.zfill(16)

            @lru_cache(None)
            def dp(pos, is_tight, prev_digit):
                if pos == 16: return 1
                
                res = 0
                upper = int(n_str[pos]) if is_tight else 9
                
                for digit in range(upper + 1):
                    new_tight = is_tight and (digit == upper)
                    
                    # If this position is on the path, we must satisfy non-decreasing property
                    if pos in path_set:
                        if digit >= prev_digit:
                            res += dp(pos + 1, new_tight, digit)
                    else:
                        # Not on the path, any digit is fine
                        res += dp(pos + 1, new_tight, prev_digit)
                return res
            
            return dp(0, True, 0)

        return count_upto(str(r)) - count_upto(str(l - 1))