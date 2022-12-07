# Intuition

like *1254. Number of Closed Islands* & *1020. Number of Enclaves*

whenever we using DFS to traverse one connected components (island), we floodfill it just like store it in a `visited` set

and increment count by 1 if it's valid

# Approach

using DFS to traverse in *grid2* to find island.

while DFS, we use a flag `isSubIsland` to check if current island in *grid2* is subisland in *grid1* or not
once we found any one of connected island is not subisland, we mark current island to `False` and return `0` count. otherwise, return `1` and update total count

# Complexity
- Time complexity:

$$O(ROWS*COLS)$$

- Space complexity:

$$O(recursion stacks)$$
