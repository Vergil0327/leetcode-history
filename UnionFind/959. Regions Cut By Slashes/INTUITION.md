# Intuition

break one cell into 4 small cells
```
["4\1/2"
 " /3\"]
```

- once we meet "/", cell-2 & cell-3 merge together and cell-1 & cell-4 merge together
- once we meet "\", cell-1 & cell-2 merge together and cell-4 & cell-3 merge together

we can iterate each cell and use union-find to group small cell first,
then group row-by-row, column-by-column using union-find too.

- each cell's cell-1 can merge with previous cell's cell-3
- each cell's cell-4 can merge with previous column's cell-2

# Complexity

- time complexity

$$O(4n^2)$$

- space complexity

$$O(4n^2)$$