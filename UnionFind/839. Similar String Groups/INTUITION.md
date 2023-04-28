# Intuition

after reading problem, we know that:
- strs[i] and strs[j] are similiar when they are **the same** or just need **1 swap**.
- we need to group together if two similiar groups share same strs[i]

thus, we can iterate through each pair, strs[i] & strs[j], in $O(n^2)$ to check if they are similiar or not first.

then, we use union-find to group similiars together.

the size of union-find groups is answer.

# Complexity
- Time complexity:
$$O(mn^2)$$

- Space complexity:
$$O(n^2)$$
