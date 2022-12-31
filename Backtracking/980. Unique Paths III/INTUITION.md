# Intuition

1. count how many steps we need to walk over
2. find starting point and start backtracking

everytime we walk over some grid, we can mark it as visited by floodfilling it with `-1`

# Complexity
- Time complexity:
$$O(4^{mn})$$

- Space complexity:
$$O(1)$$
