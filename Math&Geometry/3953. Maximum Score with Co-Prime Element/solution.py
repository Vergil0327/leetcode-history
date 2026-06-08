'''
The Core Insight

The problem states that after modifications, you must select exactly one special index i such that nums[i] is co-prime with every other element in the modified array.
Let the finalized value of nums[i] be $X$.

1. If $X$ is co-prime with every other element, it means no other element in the array can share a prime factor with $X$.
2. If another element in the array does share a prime factor with $X$, that element must be modified to some value that is co-prime with $X$. The cheapest way to change an element to make it co-prime with $X$ is to change it to 1 (since 1 is co-prime with everything). Each such change costs exactly 1.

This allows us to evaluate the cost for any chosen value $X \le \text{maxVal}$:

If $X$ originates from our original array (i.e., we picked an existing nums[i] and decided not to change its value):Any other element in the array that shares a prime factor with $X$ must be changed.$$\text{Modification Cost} = (\text{Total elements in } nums \text{ that share a prime factor with } X)$$$$\text{Score} = X - \text{Modification Cost}$$
If $X$ does NOT originate from our original array (i.e., we choose some index i, change its value to a brand new number $X \le \text{maxVal}$):We pay an initial cost of 1 to change nums[i] to $X$. Then, we pay an additional 1 for every other element in the array that shares a prime factor with $X$.$$\text{Modification Cost} = 1 + (\text{Total elements in } nums \text{ that share a prime factor with } X)$$$$\text{Score} = X - \text{Modification Cost}$$

🛠️ Optimization: Inclusion-Exclusion via Prime Factors

To find the "Total elements sharing a prime factor with $X$" efficiently for all $X \le 10^5$, we can count the multiples of prime numbers across the array using a frequency map and use the Inclusion-Exclusion Principle.
Since $X \le 10^5$, any number has at most 7 unique prime factors ($2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 > 10^5$). This means $2^7 = 128$ operations per candidate value, which runs blazing fast!


Inclusion-Exclusion Principle. 

The General Rule (The Pattern)
If you look closely at the 2-set and 3-set formulas, a distinct mathematical pattern emerges based on the number of sets you are intersecting at one time:

Intersecting 1 set at a time ($|B|, |S|, |T|$): Add ($+$)
Intersecting 2 sets at a time ($|B \cap S|, \dots$): Subtract ($-$)
Intersecting 3 sets at a time ($|B \cap S \cap T|$): Add ($+$)
Intersecting 4 sets at a time: Subtract ($-$)

The Golden Rule of PIE: > If the combination involves an odd number of sets, ADD it.
If it involves an even number of sets, SUBTRACT it.

How it applies to Code (Example: Finding Non-Coprime Numbers)

In the LeetCode problem above, we needed to find how many numbers in an array share a prime factor with a candidate number $X$.
Let's say $X = 30$. The unique prime factors of $30$ are $2, 3,$ and $5$.To find how many numbers in our array share a factor with $30$, we are looking for numbers divisible by $2$, OR $3$, OR $5$.
We use a bitmask (from 1 to 7, representing binary 001 to 111) to easily iterate through all combinations of these prime factors:

```
Mask (Binary) -> Factors Chosen       -> Product -> Set Count -> Action
------------------------------------------------------------------------
001           -> [2]                  -> 2       -> 1 (Odd)  -> ADD numbers divisible by 2
010           -> [3]                  -> 3       -> 1 (Odd)  -> ADD numbers divisible by 3
100           -> [5]                  -> 5       -> 1 (Odd)  -> ADD numbers divisible by 5

011           -> [2, 3]               -> 6       -> 2 (Even) -> SUBTRACT numbers divisible by 6
101           -> [2, 5]               -> 10      -> 2 (Even) -> SUBTRACT numbers divisible by 10
110           -> [3, 5]               -> 15      -> 2 (Even) -> SUBTRACT numbers divisible by 15

111           -> [2, 3, 5]            -> 30      -> 3 (Odd)  -> ADD numbers divisible by 30
```

By tracking the number of set bits (bits % 2 == 1), the code automatically decides whether to add or subtract the precalculated counts of multiples, yielding the exact count of overlapping numbers instantly.
'''

from collections import Counter
from typing import List

class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        # Define the absolute ceiling bound based on both constraints dynamically
        max_in_nums = max(nums) if nums else 0
        MAX_N = max(maxVal, max_in_nums) + 5
        
        # 1. Sieve Precomputation: Build square-free divisor chains and PIE signs
        p_factors = [[] for _ in range(MAX_N)]
        is_prime = [True] * MAX_N
        
        for i in range(2, MAX_N):
            if is_prime[i]:
                for j in range(i, MAX_N, i):
                    is_prime[j] = False
                    p_factors[j].append(i)
                    
        pie_items = [[] for _ in range(MAX_N)]
        for i in range(2, MAX_N):
            k = len(p_factors[i])
            if k == 0: continue

            # Generate the 2^k - 1 inclusion-exclusion combinations
            for mask in range(1, 1 << k):
                prod = 1
                bits = 0
                for idx in range(k):
                    if (mask >> idx) & 1:
                        prod *= p_factors[i][idx]
                        bits += 1
                sign = 1 if bits % 2 == 1 else -1
                pie_items[i].append((prod, sign))

        # 2. Extract frequency counts
        freq = Counter(nums)
        
        # 3. Cache divisor multiple counts across the actual range
        multiple_cnt = [0] * MAX_N
        for val, count in freq.items():
            for prod, _ in pie_items[val]:
                multiple_cnt[prod] += count

        # O(1) level PIE calculation lookups
        def count_not_coprime(x: int) -> int:
            not_coprime_total = 0
            for prod, sign in pie_items[x]:
                not_coprime_total += sign * multiple_cnt[prod]
            return not_coprime_total

        max_score = float('-inf')
        
        # Scenario A: Modify an arbitrary index's value to a brand new x (1 <= x <= maxVal)
        for x in range(1, maxVal + 1):
            not_coprime_cnt = count_not_coprime(x)
            
            if not_coprime_cnt > 0:
                # Greedy: replace an existing non-coprime element to save 1 operation cost
                cost = 1 + (not_coprime_cnt - 1)
            else:
                # Everything is already coprime; overwrite any arbitrary item
                cost = 1
                
            max_score = max(max_score, x - cost)
            
        # Scenario B: Select an existing value from nums to remain completely unchanged
        for x in freq:
            if x == 1:
                max_score = max(max_score, 1)
                continue
                
            not_coprime_cnt = count_not_coprime(x)
            # The core element itself stays untouched, so we subtract 1 from the modification penalty
            cost = not_coprime_cnt - 1
            max_score = max(max_score, x - cost)
            
        return max_score