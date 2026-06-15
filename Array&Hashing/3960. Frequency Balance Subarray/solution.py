from collections import Counter

class Solution:
    """
     we can fix the left boundary $i$ and expand the right boundary $j$ one element at a time. This allows us to update the frequency metrics dynamically in $O(1)$ constant time per step.
     To track if a subarray is "frequency balanced" in $O(1)$ time, we can maintain:
     
     - A hash map `count` to track the frequency of each distinct number in the current window $[i, j]$.
     - A secondary hash map `freq_of_freq` to track how many unique numbers share the exact same frequency $f$.

    The Valid Configurations:
    A subarray is valid if it meets either condition:
    1. Single Value: The size of counts is exactly 1.
    2. Dual-Frequency Balance: The size of freq_of_freq is exactly 2. If the two active frequencies are $f_1$ and $f_2$ (where $f_1 < f_2$), then $f_2$ must be exactly $2 \times f_1$.
    """
    def getLength(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = 1  # Any individual element is valid (length 1)
        
        # Enumerate each possible starting index i
        for i in range(n):
            counts = Counter()       # tracks: element -> frequency
            freq_of_freq = Counter() # tracks: frequency -> count of elements with this frequency
            
            # Expand the right boundary j sequentially
            for j in range(i, n):
                val = nums[j]
                
                # 1. Update frequencies dynamically
                old_f = counts[val]
                new_f = old_f + 1
                counts[val] = new_f
                
                # Update the frequency-of-frequency tracking table
                if old_f > 0:
                    freq_of_freq[old_f] -= 1
                    if freq_of_freq[old_f] == 0:
                        del freq_of_freq[old_f]
                        
                freq_of_freq[new_f] = freq_of_freq[new_f] + 1
                
                # 2. Check validity in O(1) time
                distinct_elements = len(counts)
                distinct_frequencies = len(freq_of_freq)
                
                if distinct_frequencies == 1:
                    # If all active elements share the exact same frequency,
                    # it's only valid if there's exactly 1 unique element (Example 2)
                    if distinct_elements == 1:
                        max_len = max(max_len, j - i + 1)
                        
                elif distinct_frequencies == 2:
                    # Extract the two active frequencies
                    f1, f2 = freq_of_freq.keys()
                    if f1 > f2:
                        f1, f2 = f2, f1
                        
                    # Both frequencies must be present, and f2 must be twice f1
                    if f1 * 2 == f2:
                        max_len = max(max_len, j - i + 1)
                        
        return max_len