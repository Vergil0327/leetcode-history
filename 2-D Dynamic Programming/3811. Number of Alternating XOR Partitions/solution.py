"""
dp1[i]: Number of valid alternating partitions for nums[0...i] ending with a block of XOR target1.
dp2[i]: Number of valid alternating partitions for nums[0...i] ending with a block of XOR target2.

The block XOR condition: pref[i] ^ pref[j] == target implies pref[j] == pref[i] ^ target.
"""

from collections import defaultdict


class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        
        # dp1[i] = ways to partition nums[:i] ending with target1 block
        # dp2[i] = ways to partition nums[:i] ending with target2 block
        
        # We use counters to store: How many dp states exist for a specific prefix XOR value?
        # To calculate dp1, we need previous dp2 states where (curr_pref ^ prev_pref) == target1
        # To calculate dp2, we need previous dp1 states where (curr_pref ^ prev_pref) == target2
        
        count_for_target1 = defaultdict(int) # Stores dp2 sums for XOR lookup
        count_for_target2 = defaultdict(int) # Stores dp1 sums for XOR lookup
        
        # Base case: To start the very first block (target1), 
        # it's as if we have one "dp2" state at index 0 with prefix XOR 0.
        count_for_target1[0] = 1
        
        curr_pref = 0
        res = 0
        
        for i in range(n):
            curr_pref ^= nums[i]
            
            # 1. Try to end a target1 block here
            # Need: curr_pref ^ prev_pref == target1  => prev_pref = curr_pref ^ target1
            ways1 = count_for_target1[curr_pref ^ target1] % mod
            
            # 2. Try to end a target2 block here
            # Need: curr_pref ^ prev_pref == target2  => prev_pref = curr_pref ^ target2
            ways2 = count_for_target2[curr_pref ^ target2] % mod
            
            # Update counters for the next step
            # A block ending in target1 allows the NEXT block to be target2
            count_for_target2[curr_pref] = (count_for_target2[curr_pref] + ways1) % mod
            # A block ending in target2 allows the NEXT block to be target1
            count_for_target1[curr_pref] = (count_for_target1[curr_pref] + ways2) % mod
            
            # The answer is the number of ways to end at the very last element.
            # However, the problem says "ending with target1, then target2, ...".
            # This means if the total blocks are odd, it ends in target1. 
            # If even, it ends in target2.
            if i == n - 1:
                res = (ways1 + ways2) % mod
                
        return res