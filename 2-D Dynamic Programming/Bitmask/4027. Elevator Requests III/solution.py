# Algorithm Approach:
# 1. Use Bitmask DP where dp[mask][i] stores the minimum time to fulfill the subset of requests represented by 'mask', given that request 'i' was the last one fulfilled.
# 2. Base Cases (Mask with 1 bit set):
#    For each single request i, moving from 'start' to requests[i][1] takes abs(start - requests[i][1]) seconds. 
#    The completion time is max(abs(start - requests[i][1]), requests[i][0]).
# 3. Transitions:
#    For a current mask and last visited request 'last':
#    To fulfill an unfulfilled request 'i':
#    - Travel time = dp[mask][last] + abs(requests[last][1] - requests[i][1])
#    - Arrival time at floor = requests[i][0]
#    - New completion time = max(Travel time, Arrival time)
# 4. Answer:
#    The answer is min(dp[(1<<m) - 1][i]) over all 0 <= i < m.

# Complexity:
# - Time Complexity: O(2^m * m^2), where m <= 16 (approx. 65,536 * 256 operations), running well within limits.
# - Space Complexity: O(2^m * m) for the DP table.

class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)
        states = 1 << m
        
        # dp[mask][i]: min time to visit subset 'mask' with 'i' as the last visited request
        dp = [[float('inf')] * m for _ in range(states)]
        
        # Base cases: start -> requests[i]
        for i in range(m):
            arrival, floor = requests[i]
            dp[1 << i][i] = max(abs(start - floor), arrival)
            
        # State transitions
        for mask in range(1, states):
            for last in range(m):
                if not (mask & (1 << last)): continue
                if dp[mask][last] == float('inf'): continue
                
                # Try visiting the next request 'i'
                for i in range(m):
                    if mask & (1 << i): continue
                    
                    next_mask = mask | (1 << i)
                    arrival, floor = requests[i]
                    last_floor = requests[last][1]
                    
                    reach_time = dp[mask][last] + abs(last_floor - floor)
                    fulfill_time = max(reach_time, arrival)
                    
                    dp[next_mask][i] = min(dp[next_mask][i], fulfill_time)
                    
        return min(dp[states - 1])