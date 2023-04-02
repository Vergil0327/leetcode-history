# Intuition
we can sort the potions, then for each spells[i], we can binary search its lowerbound of potion where lowerbound is first index such that spells[i] * potion[lowerbound] >= success.

-> pairs[i] = len(potion) - lowerbound

# Complexity
- Time complexity:
$$O(nlogm)$$

- Space complexity:
$$O(n)$$
