# Max Heap

## Intuition
just simulate manipulation

1. store each row as max heaps first
2. iterate through every row and find max value
3. find until row is empty

# Complexity
- Time complexity:
$$O(COLS * ROWS*log(COLS))$$

- Space complexity:
$$O(ROWS * COLS)$$

# Sorting

## Intuition

sort each rows and find max column by column.

- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(1)$$

```python
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid : row.sort()
        return sum(max(col) for col in zip(*grid))
```