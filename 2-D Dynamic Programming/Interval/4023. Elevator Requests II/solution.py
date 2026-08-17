"""
Algorithm Approach:
This problem can be modeled as Interval Dynamic Programming.
1. Filter & Sort: Remove 'start' from requests if present (since its cost is 0 and it's fulfilled at time 0), then sort the remaining requests. Insert 'start' into the sorted list to identify its position.
2. State Representation: Let the sorted requested floors (excluding 'start' if fulfilled) be R[0...m-1]. Any set of fulfilled requests forms a contiguous subsegment R[i...j] that includes 'start'.
3. Transition Cost: Instead of accumulating time for each request, use the "cost-to-come" technique: when moving a distance d between floors while there are k requests remaining unfulfilled, every unfulfilled request incurs d penalty, adding (k * d) to the total penalty.
4. DP Definition:
   - dp[l][r][0]: Minimum total accumulated penalty when the fulfilled interval is R[l...j] and the elevator is at the left endpoint R[l].
   - dp[l][r][1]: Minimum total accumulated penalty when the fulfilled interval is R[l...j] and the elevator is at the right endpoint R[r].
5. Base Case:
   - Identify where 'start' falls in the sorted requests array. Start with an interval containing just 'start' (or the insertion position) with cost 0.
6. Transitions:
   From state (i, j) with 'rem' remaining unfulfilled requests:
   - Expand left to i - 1:
     - From left (R[l]): cost = rem * (R[l] - R[l - 1])
     - From right (R[r]): cost = rem * (R[r] - R[l - 1])
   - Expand right to j + 1:
     - From left (R[l]): cost = rem * (R[r + 1] - R[l])
     - From right (R[r]): cost = rem * (R[r + 1] - R[r])


Complexity:
- Time Complexity: O(m^2), where m is the number of requests (m <= 1500).
- Space Complexity: O(m^2) for the DP table storing interval states.
"""

class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        reqs = sorted([r for r in requests if r != start])
        if not reqs:
            return 0
        
        m = len(reqs)
        
        # Find where 'start' fits in the sorted reqs list
        # pos is the index of the first element >= start
        pos = 0
        while pos < m and reqs[pos] < start:
            pos += 1
            
        # dp[i][j][0]: at reqs[i], dp[i][j][1]: at reqs[j]
        # Initialize with infinity
        INF = float('inf')
        dp = [[[INF, INF] for _ in range(m)] for _ in range(m)]
        
        # Base Cases: Start by moving from 'start' to either reqs[pos-1] or reqs[pos]
        # Option 1: Move left first to reqs[pos - 1] (if exists)
        if pos - 1 >= 0:
            dist = start - reqs[pos - 1]
            dp[pos - 1][pos - 1][0] = dist * m
            dp[pos - 1][pos - 1][1] = dist * m
            
        # Option 2: Move right first to reqs[pos] (if exists)
        if pos < m:
            dist = reqs[pos] - start
            dp[pos][pos][0] = dist * m
            dp[pos][pos][1] = dist * m
            
        for length in range(1, m):
            for l in range(m - length + 1):
                r = l + length - 1
                rem = m - length  # Number of unfulfilled requests remaining
                
                # Expand left to i - 1
                if l > 0:
                    # Move from R[i] to R[i-1]
                    cost_left = rem * (reqs[l] - reqs[l - 1])
                    dp[l - 1][r][0] = min(dp[l - 1][r][0], dp[l][r][0] + cost_left)
                    
                    # Move from R[j] to R[i-1]
                    cost_right = rem * (reqs[r] - reqs[l - 1])
                    dp[l - 1][r][0] = min(dp[l - 1][r][0], dp[l][r][1] + cost_right)
                
                # Expand right to j + 1
                if r + 1 < m:
                    # Move from R[i] to R[j+1]
                    cost_left = rem * (reqs[r + 1] - reqs[l])
                    dp[l][r + 1][1] = min(dp[l][r + 1][1], dp[l][r][0] + cost_left)
                    
                    # Move from R[j] to R[j+1]
                    cost_right = rem * (reqs[r + 1] - reqs[r])
                    dp[l][r + 1][1] = min(dp[l][r + 1][1], dp[l][r][1] + cost_right)
                    
        return min(dp[0][m - 1][0], dp[0][m - 1][1])