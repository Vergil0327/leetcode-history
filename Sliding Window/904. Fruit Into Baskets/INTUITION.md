# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
in the beginning, I got confused by the 2 type of fruits constraints.

and I saw the description says: **Once you reach a tree with fruit that cannot fit in your baskets, you must stop**

this constraint hints us about **sliding window**.

if our window less than 2 type or we already contains the type, we can keep picking which means we can move our right pointer.

once we have 2 more type, we must stop and throw out from window until our window contains 2 type only which means we must move our left pointer.

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$
