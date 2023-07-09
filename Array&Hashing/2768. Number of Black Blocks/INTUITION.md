# Intuition

because `2 <= m <= 10^5 and 2 <= n <= 10^5`, we can't iterate m*n.
thus, we count each black cell's contribution. (0 <= coordinates.length <= 10^4)

since "block" is identified with top-left cell, each black cell contributes to its top-left, left, top cell.
we can use hashmap to record contribution

```py
for r, c in coordinates:
    for i in range(r-1, r+1):
        for j in range(c-1, c+1):
            if 0 <= i < m-1 and 0 <= j < n-1:
                contrib[(i,j)] += 1
```

total_blocks = (m-1)*(n-1)
if cnt = sum(black[i] where i from 1 to 4) => cost `cnt` blocks.
rest of white blocks = total_blocks - cnt