class Solution:
    def minimumOR(self, grid: list[list[int]]) -> int:
        # We start with the goal of having 0 as the OR result.
        # We will gradually allow bits to be 1 only if necessary.
        current_or = 0
        
        # We assume 31 bits is enough for standard 32-bit integers
        for bit in range(31, -1, -1):
            # Try to see if we can keep this bit as 0.
            # The potential OR would be the bits we've already been 
            # forced to set to 1, plus any bits smaller than the current one.
            # But it's easier to check: Can we satisfy every row using 
            # ONLY bits already set in 'current_or' and bits smaller than 'bit'?
            
            test_or = current_or | ((1 << bit) - 1)
            
            possible = True
            for row in grid:
                row_possible = False
                for val in row:
                    # Check if 'val' only uses bits allowed by test_orq
                    if (val | test_or) == test_or:
                        row_possible = True
                        break
                
                if not row_possible:
                    possible = False
                    break
            
            # If we couldn't satisfy every row without this bit, 
            # then this bit MUST be 1 in our final answer.
            if not possible:
                current_or |= (1 << bit)
                
        return current_or