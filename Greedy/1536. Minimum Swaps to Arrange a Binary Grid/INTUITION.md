# Intuition

```
00000   10000
X0000   X1000
XX000   XX100
XXX00   XXX10
XXXX0   XXXX1
```

0. we don't care X position at i-th row (see above)

1. find each row's rightmost 1 and store in hashmap
now we have `rightmostOne` hashmap store: { column idx of rightmost 1: {indices of row} }

2. deal row one by one in order.
    - for current row, we can have all the row whose rightmost_1 is <= current row. let's add to hashset `validRows`
    - if validRows is empty, return -1. (empty candidate)
    - iterate all the possible row and calculate its swap distance. choose minimum swaps greedily
    - also, don't forget each time we finished current row, all the rows above current row are shift down by 1 row.
      - we should store shift in `shift` array.
      - thus, for every valid row, its swap distance is `abs(rowIdx+shift[rowIdx] - current_row_idx)`, and don't forget to update `shift` array
