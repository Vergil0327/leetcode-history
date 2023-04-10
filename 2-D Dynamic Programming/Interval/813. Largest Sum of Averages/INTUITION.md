# Intuition

we can define dp as:
`dp[i][k]: the maximum score considering nums[:i] with k partitions`

X X [X X X X X X X]
 j-1 j           i

**state transfer**
dp[i][k] = max(dp[i][k], dp[j-1][k-1] + avg(nums[j:i]))

some techniques:
    - change to 1-indexed to prevent dp[j-1][k-1] from out-of-bounds
    - k's constraints from K and i. we can't partition more than i (1-indexed)
    - j's minimum position is k considering that we must have valid k partitions

**base condition**

since we start from i=1 & k=1, we need to take care of dp[0][0], dp[0][k]

dp[0][0] = 0
consider 0 element and 0 partition -> 0 score

dp[0][k] = invalid state -> keeps default value

dp[i][k] = -inf as default value since we want to find maximum score