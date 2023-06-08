# Intuition

這題最重要的突破口是s.length的範圍很小, 只有`2 <= s.length <= 12`
所以我們可以透過backtracking來找出兩個subsequence

每個s[i]我們可以選擇加到subseq1或subseq2
這樣會有2^12種pair, 也就4096種

在找出所有可能pair後, 我們剩下的工作就是算出個別subseq內的最長palindromic subseq.

而這就是簡單的區間型dp, 我們這麼來看:

我們定義dp[i][j]為`s[i:j] (both inclusive)`這區間內的最長palindrome subseq

- 如果s[i] == s[j], 那麼我們就可以試著更新`dp[i][j] = dp[i+1][j-1] + 2`
- 如果s[i] != s[j], 那麼最長palindromic subseq.可能存在於s[i:j-1]或s[i+1:j], 也就是`dp[i][j] = max(dp[i+1][j], dp[i][j-1])`

```
X X X X X X X X X
i               j
```

那最後答案就是`dp[0][len(s)-1]`