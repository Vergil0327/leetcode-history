"""
Problem Explanation & Decomposition:

1. Input Overview:
   - You are given an array 'nums' of n integers.
   - Each number is between 0 and 2^15 - 1 (meaning it fits in 15 bits, from bit 0 to bit 14).
   - You are allowed to reorder 'nums' into ANY permutation 'perm' of your choice.

2. What is the 'power' array?
   - 'power' is an array of size 15, representing bit 14 down to bit 0.
   - Specifically:
       power[0]  corresponds to Bit 14 (most significant bit)
       power[1]  corresponds to Bit 13
       ...
       power[12] corresponds to Bit 2
       power[13] corresponds to Bit 1
       power[14] corresponds to Bit 0 (least significant bit)

3. How is power[i] calculated for a fixed permutation 'perm'?
   - power[i] is the length of the LONGEST PREFIX of 'perm' where EVERY element in that prefix has bit (14 - i) set (i.e. equal to 1).
   - In other words, if you look at bit position B = 14 - i:
       - If perm[0] has bit B = 1, perm[1] has bit B = 1, ..., perm[j-1] has bit B = 1, but perm[j] has bit B = 0:
         Then power[i] = j.
       - If ALL n elements in perm have bit B = 1, power[i] = n.
       - If perm[0] has bit B = 0, power[i] = 0.

4. Objective:
   - Find a permutation 'perm' that makes the 15-element array 'power' LEXICOGRAPHICALLY LARGEST.
   - Lexicographically largest means we want power[0] (bit 14 prefix length) to be as large as possible.
   - If there's a tie, make power[1] (bit 13 prefix length) as large as possible, then power[2], and so on down to power[14].

---

Concrete Walkthrough of Example 2:

Input: nums = [3, 1, 7] (n = 3)

Let's look at their 15-bit binary representations (showing only bits 2, 1, 0):
  7 in binary: ...000 1 1 1  (Bit 2=1, Bit 1=1, Bit 0=1)
  3 in binary: ...000 0 1 1  (Bit 2=0, Bit 1=1, Bit 0=1)
  1 in binary: ...000 0 0 1  (Bit 2=0, Bit 1=0, Bit 0=1)

Bits 14 down to 3 are 0 for all numbers. So power[0] through power[11] will all be 0 no matter what.

Now let's test the chosen permutation perm = [7, 3, 1]:

- Index 12 -> Bit 2:
  Check perm elements for Bit 2:
    perm[0] = 7 -> Bit 2 is 1
    perm[1] = 3 -> Bit 2 is 0  <-- Streak breaks at index 1!
  Longest prefix with Bit 2 = 1 has length 1.
  So power[12] = 1.

- Index 13 -> Bit 1:
  Check perm elements for Bit 1:
    perm[0] = 7 -> Bit 1 is 1
    perm[1] = 3 -> Bit 1 is 1
    perm[2] = 1 -> Bit 1 is 0  <-- Streak breaks at index 2!
  Longest prefix with Bit 1 = 1 has length 2.
  So power[13] = 2.

- Index 14 -> Bit 0:
  Check perm elements for Bit 0:
    perm[0] = 7 -> Bit 0 is 1
    perm[1] = 3 -> Bit 0 is 1
    perm[2] = 1 -> Bit 0 is 1
  ALL 3 elements have Bit 0 = 1!
  So power[14] = 3.

Resulting power array: [0,0,0,0,0,0,0,0,0,0,0,0, 1, 2, 3]

The Intuition: Sequential Bottleneck Partitioning

1. Think of the array as a pipeline:
   - We want to make power[0] (bit 14's prefix) as long as possible.
   - To do that, we move ALL elements with bit 14 = 1 to the front.
   - The elements with bit 14 = 1 form "Group 1", and elements with bit 14 = 0 form "Group 2".

2. What breaks a streak?
   - As we scan left-to-right through our groups for a given bit 'b':
     * If a group has ALL 1s for bit 'b', the streak passes straight through it!
     * The FIRST group that contains a 0 is the BOTTLENECK. 
     * Inside that bottleneck group, we split it into [1s, 0s].
     * The streak STOPS at the 0s inside that bottleneck group.

3. Why do we ignore groups AFTER the bottleneck?
   - Once bit 'b' hits a 0 in the bottleneck group, power[14 - b] is officially LOCKED. 
   - No matter how we arrange elements in subsequent groups, bit 'b' can NEVER reach them because the prefix streak was already broken!
   - Therefore, we NEVER split any groups that come after the bottleneck for bit 'b'. Their order remains completely free to be optimized for lower bits!

4. Iterative Refinement across 15 Bits:
   - Bit 14 splits the array into 2 groups (or 1 if all are 1s / all are 0s).
   - Bit 13 looks at these groups, passes through full-1 groups, splits the bottleneck group into two smaller groups, and leaves remaining groups untouched.
   - By Bit 0, we have an ordered sequence of fine-grained groups, and power[0..14] is guaranteed to be lexicographically maximal!

Complexity Analysis
Time Complexity: $\mathcal{O}(15 \cdot N)$For each of the 15 bits, we iterate through each element in $N$ exactly once.Total operations $\approx 15 \times 50,000 = 7.5 \times 10^5$, completing in < 0.01s (eliminating any TLE).
Space Complexity: $\mathcal{O}(N)$ space to store the groups.
"""

# Divide & conquer

class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        # Bitwise Radix Partitioning / Trie Ordering
        def arrange(arr: list[int], bit: int) -> list[int]:
            if not arr or bit < 0:
                return arr
            
            ones = [x for x in arr if (x >> bit) & 1]
            zeros = [x for x in arr if not ((x >> bit) & 1)]
            
            return arrange(ones, bit - 1) + arrange(zeros, bit - 1)

        perm = arrange(nums, 14)

        power = [0] * 15
        for i in range(15):
            b = 14 - i
            streak = 0
            for x in perm:
                if (x >> b) & 1:
                    streak += 1
                else:
                    break
            power[i] = streak

        return power