# Intuition

3 cases to consider:
1. all zeros
2. all ones
3. zeros followed by ones

first, count total `0` to see how many flips we need for **case 2**

also, we can know the flips we need for **case 1** by `len(s) - total zeros`

for **case3**, we use prefix1 and suffix0 to calculate how many flips we need if we want to make all s[:i] be zeros and make all s[i:] be ones

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$
