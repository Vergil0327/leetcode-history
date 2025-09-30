from itertools import accumulate

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        
        # Shift range
        range_size = r - l
        r = range_size
        l = 0
        
        # Initialize: all values are 1
        dp0 = [1] * (r + 1)
        dp1 = [1] * (r + 1)
        
        for iteration in range(1, n):
            next_dp0 = [0] * (r + 1)
            next_dp1 = [0] * (r + 1)
            
            # Compute all dp1 values efficiently
            running_sum = 0
            for num in range(r + 1):
                next_dp1[num] = running_sum
                running_sum = (running_sum + dp0[num]) % mod
            
            # Compute all dp0 values efficiently  
            running_sum = 0
            for num in range(r, -1, -1):
                next_dp0[num] = running_sum
                running_sum = (running_sum + dp1[num]) % mod
            
            dp0 = next_dp0
            dp1 = next_dp1
        
        # Sum all final values
        return sum(dp0[i] + dp1[i] for i in range(r + 1)) % mod