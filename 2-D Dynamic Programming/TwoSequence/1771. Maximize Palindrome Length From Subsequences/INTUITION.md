# Intuition

由於我們要找一個在word1的subseq.跟一個在word2的subseq.組成的最長palindrome，那其實我們可以把word1跟word2拼接起來然後找一段最長的palindrome，然後限制左右端點得分別落在word1及word2內

words = [XXXXXXXXXX][YYYYYYYYYYY]
            word1       word2

對於一個palindrome，我們可以這樣定義

dp[l][r]: the maximum length of palindrome for words[l:r]

如果words[l] == words[r]，那代表我們可以從dp[l+1][r-1]額外再加上這兩個字符拼成palindrome，亦即:

`dp[l][r] = dp[l+1][r-1] + 2`

那如果words[l] != words[r]，代表words[l:r]的最長palindrome存在於words[l+1:r]或words[l:r-1]，因此:

`dp[l][r] = max(dp[l+1][r], dp[l][r-1])`

所以總結來說就是:

```py
if words[l] == words[r]:
    dp[l][r] = dp[l+1][r-1] + 2
else:
    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
```

那在這之中，由於我們要找符合條件的最長palindrome，所以我們可以在更新DP的時候順便確認是不是符合條件的palindrome，是的話就紀錄下來找最大的

```py
if words[l] == words[r]:
    dp[l][r] = dp[l+1][r-1] + 2
    if l < len(word1) and r >= len(word1):
        answer = max(answer, dp[l][r])
```

# Complexity

- time complexity
$$O((len(word1)+len(word2))^2)$$

- space complexity
$$O(len(word1)+len(word2))$$