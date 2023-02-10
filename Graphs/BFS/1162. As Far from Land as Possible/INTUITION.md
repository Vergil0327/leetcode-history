# Intuition

whenever there exsits a start and a end position.
we can think forward and bacward direction and choose better way to go.

take grid below as example, we can start from the land and keep expanding.
we can get the answer from the steps we need to turn all the water(0) into land(1).

just be careful of the edge case: `all-1-grid`
if all the cell is land, distance will be `0`

```
# Grid
1 0 0 0 1
0 0 0 0 0
1 0 0 0 1

1 1 0 1 1
1 0 0 0 1
1 1 0 1 1

1 1 1 1 1
1 1 0 1 1
1 1 1 1 1

1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
```

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
$$O(n^2)$$

- Space complexity:
$$O(n^2)$$
