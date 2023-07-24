# Intuition

對於nums[i]來說, 可以接在nums[j]後面
如果index=j, 有dp[j]個subseq., 那dp[i] += dp[j]

定義dp[i]: the number of distinct non-empty subsequences of s[:i]

那狀態轉移就是:
對於結尾在s[i]的subseq.來說, s[i]可以接在dp[i-1]個subseq.後面, 以及自己本身自立門戶
dp[i] = dp[i-1] + 1

然後再加上到i-1為止的所有subseq
dp[i] += dp[i-1]

但由於這樣會有重複的subseq., 所以我們還需要紀錄其他狀態

我們額外紀錄每個subseq.最後結尾是在哪個字符上,
由於結尾不同, 所以個別都會是distinct的

定義dp[i][ch]: the number of distinct non-empty subsequences of s[:i] and ended with `ch`
其中ch最多26個小寫英文字母

所以在每一輪, 我們可以查看一下26個字母ch:

那這樣對於s[i]來說:

他可以接在sum(dp[i-1])個subseq.後面, 以及s[i]本身自立門戶, 藉此組成結尾於s[i]的subseq.
dp[i][s[i]] = sum(dp[i-1]) + 1

那對於其他字母結尾的subseq.的話
dp[i][ch] = dp[i-1][ch] where ch != s[i]

那最終答案就是sum(dp[i-1])
