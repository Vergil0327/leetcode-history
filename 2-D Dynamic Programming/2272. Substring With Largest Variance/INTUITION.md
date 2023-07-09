# Intuition

variance = difference of occurrence/frequency of any two of characters in Counter(s)
we want largest variance amoung all the substring of s

在subarray中比對任兩個字母的occurence difference
把其中一個字母想成+1, 另一個想成-1, 其餘視作為+0
透過Kadane可求出subarray sum, 亦即兩個字母的occurence difference

遍歷所有字母可能後即可求出`s`裡任兩個字母的variance, 找出全局最大即可

Kadane: dp[i] = max(nums[i], dp[i-1] + nums[i]) => 截至i為止的最大subarray sum
由於我們必須保證至少兩個字母都必須出現
ex. 我們要求出"a"跟"b"在s中的variance
如果s="aaab", 那麼前面的"aaa"雖然是`+3`, 但由於裡面一個b都沒有, 並不符合variacne的定義
所以我們定義:
dp[i][0]: maximum subarray sum ended at i
dp[i][1]: maximum subarray sum ended at i and contains 1 "b" character at least

那麼
"a"視作`+1`, "b"視作`-1`, 其餘字符不考慮variance, 視作`+0`
- 如果當s[i] == "a":
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + 1
- 如果當s[i] == "b":
    dp[i][0] = 0
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]) - 1
- 其餘字母
    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-1][1]