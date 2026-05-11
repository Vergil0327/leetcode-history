"""
This problem involves simulating the growth of a set of points in 3D space.
Given the extremely small constraints ($x, y, z \le 6$ and points.length <= 20), the total state space is very limited.
A point can only exist if its coordinates are within the range $[0, 6]$, meaning there are only $7 \times 7 \times 7 = 343$ possible unique points.

The Strategy: BFS Simulation

Since we need the smallest integer $k$, this is a Breadth-First Search (BFS) problem. However, unlike a standard BFS where you move from one point to another, here a "generation" consists of all possible pairs from the entire existing pool.

1. Generation 0: Check if the target is already in the starting set.
2. Generation $k$: Take the set of all points discovered up to generation $k-1$. Form every possible pair of distinct points, calculate their midpoint using the floor formula, and add these to the set.
3. Termination:
    - If the target is added, return the current $k$.
    - If a new generation produces no new points, and the target hasn't been found, it is impossible. Return -1.
"""
class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        target_tuple = tuple(target)
        # Convert initial points to tuples for hashability
        current_points = {tuple(p) for p in points}
        
        # Generation 0 check
        if target_tuple in current_points: return 0
        
        # If there's only one point and it's not the target, we can never pair it
        if len(current_points) < 2: return -1
            
        k = 0
        while True:
            k += 1
            new_gen = set()
            # Convert set to list to iterate and create pairs
            points_list = list(current_points)
            n = len(points_list)
            
            # Form every possible pair from ALL points accumulated so far
            for i in range(n):
                for j in range(i + 1, n):
                    p1 = points_list[i]
                    p2 = points_list[j]
                    
                    # Compute c = [floor((x1 + x2) / 2), ...]
                    # In Python, // 2 performs floor division for positive integers
                    mid = (
                        (p1[0] + p2[0]) // 2,
                        (p1[1] + p2[1]) // 2,
                        (p1[2] + p2[2]) // 2
                    )
                    
                    if mid not in current_points:
                        new_gen.add(mid)
            
            # If target found in this batch of new points
            if target_tuple in new_gen: return k
            
            # If no new points were discovered, we've reached a fixed point
            if not new_gen: break
                
            # Add new points to the pool for the next generation
            current_points.update(new_gen)
            
        return -1