# Intuition

Core concept is just normal BFS shortest path problem

since array is not hashable, we can transform array to `str` for us to do BFS

thus, we turn 2-D array such as `[[1,2,3],[4,5,0]]` into `"123450"`

as for neighbor nodes, we can observe that the rule of how we can swap two nodes is predictable. we can define a helper function `genNext` to help us find neighbor nodes.

```
[0,2,3,
 4,5,1]

index = 0 -> can swap with 1, 3
index = 1 -> can swap with 0, 2, 4
... and so on
```

once we found current string equals to `"123450"`, we can return how many moves we make so far.

# Approach

use BFS to find minimum moves for us to reach target

# Complexity
- Time complexity:
$$O((ROWS * COLS)!)$$

- Space complexity:
$$O((ROWS * COLS)!)$$

