from collections import Counter

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = 0
        total_counts = Counter()
        
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                total_sum += val
                total_counts[val] += 1

        def check_valid(s1, s2, rows, cols, f1, ends, is_section_two=False):
            """
            s1: Sum of the section we are testing for a discount
            s2: Sum of the other section
            f1: Frequency map of Section 1 (Top or Left)
            ends: The values at the boundaries of the current section
            is_section_two: If True, we calculate Section 2's freq using (Total - f1)
            """
            if s1 == s2:
                return True
            
            target = s1 - s2
            if target <= 0:
                return False
            
            # Find if target exists in the specific section
            if not is_section_two:
                exists = f1.get(target, 0) > 0
            else:
                exists = (total_counts.get(target, 0) - f1.get(target, 0)) > 0
                
            if not exists:
                return False
            
            # Connectivity Logic:
            # If the section is a 2D block, any cell removal is safe.
            if rows > 1 and cols > 1:
                return True
            
            # If the section is 1D, target must be one of the two ends.
            return target in ends

        # --- 1. Horizontal Cuts ---
        top_sum = 0
        top_counts = Counter()
        for r in range(m - 1):
            # Update top section with the new row
            for c in range(n):
                val = grid[r][c]
                top_sum += val
                top_counts[val] += 1
            
            bottom_sum = total_sum - top_sum
            
            # Check Top Section (Ends are corners of top rectangle)
            if check_valid(top_sum, bottom_sum, r + 1, n, top_counts, 
                           {grid[0][0], grid[0][n-1], grid[r][0], grid[r][n-1]}):
                return True
            
            # Check Bottom Section (Ends are corners of bottom rectangle)
            if check_valid(bottom_sum, top_sum, m - 1 - r, n, top_counts, 
                           {grid[r+1][0], grid[r+1][n-1], grid[m-1][0], grid[m-1][n-1]}, True):
                return True

        # --- 2. Vertical Cuts ---
        left_sum = 0
        left_counts = Counter()
        for c in range(n - 1):
            # Update left section with the new column
            for r in range(m):
                val = grid[r][c]
                left_sum += val
                left_counts[val] += 1
            
            right_sum = total_sum - left_sum
            
            # Check Left Section
            if check_valid(left_sum, right_sum, m, c + 1, left_counts, 
                           {grid[0][0], grid[m-1][0], grid[0][c], grid[m-1][c]}):
                return True
            
            # Check Right Section
            if check_valid(right_sum, left_sum, m, n - 1 - c, left_counts, 
                           {grid[0][c+1], grid[m-1][c+1], grid[0][n-1], grid[m-1][n-1]}, True):
                return True

        return False