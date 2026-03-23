"""
"Meet-in-the-middle" is an optimization technique used when the input size (like your $N=40$) is too large for a standard brute-force approach ($2^{40}$ is about 1 trillion operations) but small enough that you can split it into two halves.
By splitting the array into two parts of 20 elements each, you only need to perform $2^{20} + 2^{20}$ operations (about 2 million), which is well within the time limit.

How Meet-in-the-Middle works for XOR
The goal is to find a subset of nums that XORs to target. Let's split nums into left_half and right_half.


1. Generate all possible XOR sums for the left_half and store them in a hash map. The map should store {xor_sum: max_subset_size}.
2. Generate all possible XOR sums for the right_half.
3. The "Meet": For every XOR sum $S_R$ found in the right half, we need to find an $S_L$ from the left half such that:
    $$S_L \oplus S_R = \text{target}$$
    
    By the properties of XOR, this is equivalent to:
        $$S_L = \text{target} \oplus S_R$$
4. If target ^ S_R exists in our left-half map, we've found a valid subset. Its total size is left_map[target ^ S_R] + right_subset_size.
"""

class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = n // 2
        
        def get_xor_counts(arr):
            # {xor_sum: max_elements_used}
            counts = {0: 0}
            for x in arr:
                new_counts = counts.copy()
                for xor_sum, elements in counts.items():
                    new_sum = xor_sum ^ x
                    new_counts[new_sum] = max(new_counts.get(new_sum, 0), elements + 1)
                counts = new_counts
            return counts

        # Step 1: Process both halves
        left_map = get_xor_counts(nums[:mid])
        right_map = get_xor_counts(nums[mid:])
        
        max_remaining = -float('inf')
        
        # Step 2: The "Meet"
        for s_r, count_r in right_map.items():
            needed_l = target ^ s_r
            if needed_l in left_map:
                max_remaining = max(max_remaining, left_map[needed_l] + count_r)
        
        return n - max_remaining if max_remaining != -float('inf') else -1