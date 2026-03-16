"""
The Actual Logic: Connecting the Two Largest Groups
The true intent of the problem is to connect the two largest distinct components by placing a point $(x, y)$ such that $x$ belongs to Group A and $y$ belongs to Group B.

Since we can pick any integer coordinate $(x, y)$, we can always find a coordinate that "bridges" two groups, unless those two groups are already the same group.

1. Group all points using DSU (merging by shared $X$ and shared $Y$).
2. Calculate the size of each resulting component.
3. Find the two largest sizes.
4. Result: $Size_1 + Size_2 + 1$.(If there is only one component, the result is $Size_1 + 1$).
"""

from collections import defaultdict

class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        sz = [1] * n

        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                if sz[root_i] < sz[root_j]: root_i, root_j = root_j, root_i
                parent[root_j] = root_i
                sz[root_i] += sz[root_j]

        # Step 1: Correctly merge by both X and Y
        xs, ys = defaultdict(list), defaultdict(list)
        for i, (x, y) in enumerate(points):
            xs[x].append(i)
            ys[y].append(i)
        
        for group in xs.values():
            for i in range(1, len(group)): union(group[0], group[i])
        for group in ys.values():
            for i in range(1, len(group)): union(group[0], group[i])

        # Step 2: Collect unique component sizes
        component_sizes = []
        visited_roots = set()
        for i in range(n):
            root = find(i)
            if root not in visited_roots:
                component_sizes.append(sz[root])
                visited_roots.add(root)

        # Step 3: Sort sizes descending
        component_sizes.sort(reverse=True)

        # Step 4: We can always bridge the two largest components
        if len(component_sizes) >= 2:
            return component_sizes[0] + component_sizes[1] + 1
        else:
            return component_sizes[0] + 1
        

# TLE
# O(n^2)
# class Solution:
#     def maxActivated(self, points: list[list[int]]) -> int:
#         n = len(points)
#         parent = list(range(n))
#         size = [1] * n

#         def find(i):
#             if parent[i] == i: return i
#             parent[i] = find(parent[i])
#             return parent[i]

#         def union(i, j):
#             root_i, root_j = find(i), find(j)
#             if root_i != root_j:
#                 if size[root_i] < size[root_j]:
#                     root_i, root_j = root_j, root_i
#                 parent[root_j] = root_i
#                 size[root_i] += size[root_j]

#         # 1. Connect points sharing X or Y
#         xs, ys = defaultdict(list), defaultdict(list)
#         for i, (x, y) in enumerate(points):
#             xs[x].append(i)
#             ys[y].append(i)
        
#         for group in xs.values():
#             for i in range(1, len(group)): union(group[0], group[i])
#         for group in ys.values():
#             for i in range(1, len(group)): union(group[0], group[i])

#         # 2. Map X/Y coordinates to the component IDs they touch
#         x_to_comps = defaultdict(set)
#         y_to_comps = defaultdict(set)
        
#         for i, (x, y) in enumerate(points):
#             root = find(i)
#             x_to_comps[x].add(root)
#             y_to_comps[y].add(root)

#         # 3. Calculate max points by picking one x and one y
#         # We want to maximize: (sum of sizes in x_to_comps[x]) + (sum of sizes in y_to_comps[y])
#         # Subtracting any component that appears in BOTH sets to avoid double counting.
        
#         def get_sum(comp_set):
#             return sum(size[c] for c in comp_set)

#         max_val = 0
#         # Optimization: Pre-calculate sums for each X and Y
#         x_sums = {x: get_sum(comps) for x, comps in x_to_comps.items()}
#         y_sums = {y: get_sum(comps) for y, comps in y_to_comps.items()}

#         # Simple approach: check all existing X and Y lines
#         # Also consider a new X or new Y that touches nothing (size 0)
#         for x in x_to_comps:
#             for y in y_to_comps:
#                 current = x_sums[x] + y_sums[y]
#                 # Subtract overlap (components that exist at both this x and this y)
#                 overlap = x_to_comps[x].intersection(y_to_comps[y])
#                 current -= sum(size[c] for c in overlap)
#                 max_val = max(max_val, current)

#         return max_val + 1