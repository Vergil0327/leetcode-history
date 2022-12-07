### Intuition

we can start **DFS** from exterior border, and turn all the node connected with border to `0`

after traverse all 4 border, we sum up the remain `1`

time: O(ROWS * COLS)
space: O(1), only `dirs` array