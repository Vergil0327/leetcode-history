# Intuition


think as knapsack problem since `n` columns only depends on `n-1` columns.
and m is just 5 at most, we can use bitmask to represent color_state for each m row.

RGB -> 3 colors
color_state <= 3 ** 5

ex. state = 124, we can get bitmask by doing:
```
bitmask = []
for i in range(m):
    bitmask.append(state%3)
    state //= 3
```

thus, `dp[n][color_state] += dp[n-1][prev_state] if no two adjacent cells having the same color`

and we can use two dp array to represent dp[n] and dp[n-1]
but be careful of intial value

if we are use dp[n][color_state] += dp[n-1][prev_state] 
every intial value of dp[n][color_state] is 0

but if we only use 2 dp array and swap them, we should clear nextDp array each iteration

```py
for _ in range(n):
    for colorState in validStates:
        # !!! initial value should be 0 because of `+=`
        # we need to clear value of nextDp[state] or we'll sum up duplicate values
        nextDp[colorState] = 0
        for prevState in validStates:
            # update DP state
```

# Other Solution

we can use 2 bits to represent color state

COLOR = [1,2,3] # [R, G, B]
      = [00, 01, 11] # in binary format

and we can use these two helper functions to set&get the color state

```py
def getColor(mask, pos):  # Get color of the `mask` at `pos`, use 2 bits to store a color
    return (mask >> (2 * pos)) & 3

def setColor(mask, pos, color):  # Set `color` to the `mask` at `pos`, use 2 bits to store a color
    return mask | (color << (2 * pos))
```

and the core structure of the algorithm is:

```py
def dp(col, prevColMask):
    if col == n: return 1  # Found a valid way
    
    ans = 0
    for nei in neighbor(prevColMask):
        ans = (ans + dp(col + 1, nei)) % 1_000_000_007
    return ans
return dp(0, 0)
```

use `neighbor` to find every valid next state

