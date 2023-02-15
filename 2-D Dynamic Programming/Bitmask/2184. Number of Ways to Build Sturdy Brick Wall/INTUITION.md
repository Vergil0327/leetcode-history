# Intuition

1. since all the values of bricks are unique, we can safely choose any of bricks to build wall
2. we can't put the same bricks at same position or the wall will not be sturdy

bricks[i] <= 10, if we want to use bitmask, must use 10-bit mask to represent used bricks[i] and its order.
10 ** 10 is too large for time and space -> think other way

we can observe that wall width is also 10 -> if we use bitmask 1<<10 to represent wall state, 2^10 is totally fine for us.

thus, we can use use bitmask to represent the wall state. since we care about the join position of wall, we can use bitmask to represent it

ex.
0000000010 -> brick's join position is 1-th position -> brick width width=9 + brick with width=1

thus, we can define dp as:
`dp[row][wall_state]: the number of ways to build sturdy wall for first i rows and use wall_state for i-th row`

and state transfer function is:
`dp[row][wall_state] += dp[row-1][wall_state'] for all wall_state' & wall_state = 0`