from collections import Counter

class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        count = Counter(planks)
        unique_heights = list(count.keys())
        
        # pair_width[H] stores the max pairs that sum to height H
        pair_width = Counter()
        
        # Calculate pair contributions for every pair of distinct/same heights
        for i in range(len(unique_heights)):
            x = unique_heights[i]
            
            # 1. Pairs formed by two planks of the same height x
            pair_width[2 * x] += count[x] // 2
            
            # 2. Pairs formed by planks of height x and height y (x != y)
            for j in range(i + 1, len(unique_heights)):
                y = unique_heights[j]
                pair_width[x + y] += min(count[x], count[y])
        
        # Candidate target heights are either an original plank height or a combined sum
        all_target_heights = set(count.keys()) | set(pair_width.keys())
        
        max_width = 0
        for H in all_target_heights:
            total_fence = count[H] + pair_width[H]
            max_width = max(max_width, total_fence)
            
        return max_width