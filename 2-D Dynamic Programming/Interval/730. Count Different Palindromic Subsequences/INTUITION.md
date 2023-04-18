# Intuition

dfs(l, r): s[l:r+1]這段區間所能組成的palindromic subsequence數目

```                   l > r -> 區間不合法
             Y        l = r -> 1
        Y         Y   l < r, 0 X -> dfs(l+1, r-1) + 2 (only Y and YY)
        Y    X    Y   l < r, 1 X -> dfs(l+1, r-1) + 2
        Y   X X   Y   l < r, 2 X -> dfs(l+1, r-1) + 2
        Y  X X X  Y   l < r, 3 X -> dfs(l+1, r-1) + 2
        Y X X X X Y   當s[l] == s[r]時,
                      dfs(l+1, r-1)這些合法palindromic subseq都可以跟s[l], s[r]組成palindromic subsequence
                      額外`+2`是加上Y跟YY這兩種情況

                      並且根據constraints, Y 只可能是"a", "b", "c", "d"
        a         a
        b         b
        c         c
        d         d
```

# bottom-up

here's an explanation of the intuition behind the algorithm:

The key insight behind this dynamic programming solution is to consider the problem of counting palindromic subsequences as a subproblem of counting all possible subsequences of the input string s.

To count all possible subsequences of s, we can use a simple dynamic programming algorithm. Let dp[i] be the number of subsequences of s that end at index i. Then we can compute dp[i] as follows:

- If we include s[i] in the subsequence, then the subsequence can be any subsequence that ends at i-1, plus the new subsequence consisting of just s[i]. Therefore, we have dp[i] = dp[i-1] * 2 + 1.
- If we exclude s[i] from the subsequence, then the subsequence can be any subsequence that ends at i-1. Therefore, we have dp[i] = dp[i-1].

Using this algorithm, we can compute the total number of subsequences of s in O(n) time, where n is the length of the input string.

Now let's consider the problem of counting palindromic subsequences of s. We can use a similar dynamic programming algorithm to compute this. Let dp[i][j] be the number of palindromic subsequences of s[i:j+1]. Then we can compute dp[i][j] as follows:

- If s[i] == s[j], then there are three cases:
  - The palindromic subsequences of s[i:j+1] that do not include s[i] or s[j] are the same as the palindromic subsequences of s[i+1:j]. Therefore, we have dp[i][j] = dp[i+1][j-1].
  - The palindromic subsequences of s[i:j+1] that include only one of s[i] and s[j] are just the single character s[i] or s[j]. Therefore, we have dp[i][j] = dp[i+1][j-1] + 2.
  - The palindromic subsequences of s[i:j+1] that include both s[i] and s[j] are just the palindromic subsequences of s[i+1:j] plus the two new palindromic subsequences consisting of s[i] and s[j] alone. However, we must subtract the palindromic subsequences that are counted twice, which are those that include s[i], s[j], and one or more characters between them. Therefore, we have dp[i][j] = dp[i+1][j-1] * 2 - dp[left+1][right-1].
- If s[i] != s[j], then the palindromic subsequences of s[i:j+1] are just the palindromic subsequences of s[i+1:j] plus the palindromic subsequences of s[i:j-1], minus the palindromic subsequences of s[i+1:j-1]. This is because any palindromic subsequence of s[i:j+1] must either include s[i] or s[j], but not both, and we must subtract the palindromic subsequences

The purpose of using left and right variables is to identify the next occurrence of the current character in the left and right directions, respectively. This allows us to calculate the number of new palindromic subsequences that can be formed using the current character.

For example, let's say we are currently processing the first occurrence of character 'a' in the string. The next occurrence of 'a' in the left direction can be identified by left[a], and the next occurrence in the right direction can be identified by right[a]. If the next occurrence of 'a' in the left direction is at index i and the next occurrence in the right direction is at index j, then we can form new palindromic subsequences of the form "a...a", "a...aa...a", "a...aaa...a", and so on, where the dots represent any character between the two 'a's. The number of new palindromic subsequences that can be formed using the current character 'a' is 2 + dp[i+1][j-1], where dp[i+1][j-1] represents the number of palindromic subsequences that can be formed using the substring between the next occurrence of 'a' in the left direction and the next occurrence of 'a' in the right direction.