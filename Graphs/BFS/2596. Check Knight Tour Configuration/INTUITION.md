# Intuition
1. floodfill every cell that our knight successfully visited
```py
if grid[r][c] == step:
    grid[r][c] = 0
```

2. move our knight to valid cell only.
    - if we can't reach the cell in required step, it means we've already failed to reach every cell

```py
if grid[row][col] != step + 1: continue
```

# Complexity
- Time complexity:
$$O(ROWS * COLS)$$

- Space complexity:
$$O(ROWS * COLS)$$
