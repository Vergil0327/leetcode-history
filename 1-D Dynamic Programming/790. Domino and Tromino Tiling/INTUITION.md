# Intuition

**DP Definition**

`dp[i]: the maximum ways for tiling board 2 x i `

困難點在於要發現狀態轉移方程:
```
dp[i] = d[i-1] + dp[i-2] + 2 * (dp[i-3] + dp[i-4] + ... + dp[0])
      = d[i-1] + dp[i-2] + 2 * presumDP[i-3]
```

n=1 |
n=2 ||, =
n=3 |||, |=, =|, 2*「」

for`「」`+ `|` -> `|「」` or `「」|`
for `「」`+ `=` -> `「」=`, `「=」`

**Base Case**

dp from 1 to n:
dp[0] = 1, for 2x0 board, 1 way to tile. (use zero tile)
dp[1] = 1, for 2x1 board, 1 way to tile
dp[2] = 2

# Complexity

- time complexity:
$$O(n)$$

- space complexity
$$O(n)$$