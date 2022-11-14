#### Union-Find

[video explanation by HuifengGuan](https://www.youtube.com/watch?v=HAaik49m0q0&ab_channel=HuifengGuan)

How many stones we can remove ?

[XXXX  XX  XX] -> [XX(X3)(X4)  X(X4)  X(X4)] -> [X19]
[  XX   X   X] -> [                        ] -> []
[  XX   X   X] -> [                        ] -> []
[   X   X   X] -> [                        ] -> []

Aaswer: 18

analysis: 
  1. we can remove column by column
  2. then, remove row by row until one stone left

so, what we want to find is every group's size - 1 since we can remove last stone in each group.
therefore, we can use union-find to solve this problem

1. we union column by column
2. then union row by row
3. find every group's parent group
4. `sum(group size - 1)` or `stones.size-groups.size` is what we want.
5. answer is `19-1`

#### DFS

so based on the analysis above, this is a connected component problem
ans: `# of stones - # of connected components`