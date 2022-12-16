# Intuition

simple version of [72. Edit Distance](../72.%20Edit%20Distance/). (only deletion)

## definition

`dp[i][j]: min deletion to make word1[:i] and word2[:j] equal`

## base case

- word1 = "", word2 = "": dp[0][0] = 0
- word1 = "", word2 = "...": dp[0][j] = j, we need to delete j characters to make them equal
- word1 = "XXXXX", word2 = "": dp[i][0] = i, we need to delete i characters to make them equal

## state transfer

if word1[i] == word2[j], we don't need to delete: `dp[i][j] = dp[i-1][j-1]`
else: `dp[i][j] = min(dp[i-1][j], dp[i][j-1])`

# Complexity
- Time complexity:
$$O(mn)$$

- Space complexity:
$$O(mn)$$

# Other Approach

1. calculate length of Longest Increasing Subsequence(LIS)
2. min steps = m-len(LIS) + n-len(LIS)

# Code
```
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        word1 = "#" + word1
        word2 = "#" + word2

        # dp[i][j]: the min delete steps to make word1[:i] and word2[:j] equal
        dp = [[0] * (n+1) for _ in range(m+1)]

        # base case
        # word1[:i] = "", word2[:j] = "XXXX" => dp[0][j] = j, we need to delete j characters to make word2 equals to word1
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]
```