# Intuition

for each cell, we can move to 4 direction and form a path
use DFS to explore:
- it's valid answer 'if length >= 4 and path can form a cycle which means we visited again

but it can happen like this:

 X->X X X X X X X X
          X       X
          X       X
          X X X X X

thus, we should record legnth at each position.
when we reach visited position again and form a cycle:
```
cycle size = total length - length at visited point
           = (dist[(row, col)]+1) - dist[(visited_row, visited_col)] + 1 # both inclusive
```

since we can't go back, we need to keep track of previous position during DFS