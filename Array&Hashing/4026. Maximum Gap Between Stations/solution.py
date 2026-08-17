"""
Algorithm Approach:
To find the maximum possible gap between two consecutive workers, we can use a Two-Pass Greedy approach:
1. Left-to-Right Pass: Compute 'earliest[i]' for each worker i by greedily picking the first matching character in 'station' that comes after worker i - 1's position.
2. Right-to-Left Pass: Compute 'latest[i]' for each worker i by greedily picking the last matching character in 'station' that comes before worker i + 1's position.
3. Maximum Gap Calculation: For each adjacent pair (i - 1, i), worker i - 1 can be placed as early as 'earliest[i - 1]' and worker i can be placed as late as 'latest[i]'. The maximum gap between them is 'latest[i] - earliest[i - 1]'. We take the maximum across all i from 1 to n - 1.

Complexity:
- Time Complexity: O(n + m) — Two single scans over the 'station' string.
- Space Complexity: O(n) — To store the earliest and latest station arrays.
"""
class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n, m = len(skill), len(station)
        if n == 1:
            return 0
        
        earliest = [0] * n
        latest = [0] * n
        
        # Pass 1: Compute earliest valid station for each worker
        st_idx = 0
        for i in range(n):
            while st_idx < m and station[st_idx] != skill[i]:
                st_idx += 1
            earliest[i] = st_idx
            st_idx += 1  # Next worker must be strictly to the right
        
        # Pass 2: Compute latest valid station for each worker
        st_idx = m - 1
        for i in range(n - 1, -1, -1):
            while st_idx >= 0 and station[st_idx] != skill[i]:
                st_idx -= 1
            latest[i] = st_idx
            st_idx -= 1  # Next worker (going left) must be strictly to the left
            
        # Calculate the maximum gap between any two adjacent workers
        max_gap = 0
        for i in range(1, n):
            max_gap = max(max_gap, latest[i] - earliest[i - 1])
            
        return max_gap