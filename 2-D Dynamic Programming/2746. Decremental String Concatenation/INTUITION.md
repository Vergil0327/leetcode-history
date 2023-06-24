# Intuition

這題狀態轉移已經很明確地告訴你對於words[i]來說只有兩種可能:
1. join(str, words[i])
2. join(words[i], str)

那既然這樣top-down dp就很明確了

對於words[i]來說, 他可以接在前面也可以接在後面
- 接在後面的話, 我們僅需要關注str[-1]跟words[i][0]
- 接在前面的話, 我們僅需要關注str[0]跟words[i][-1]

所以很明顯的我們的top-down還需要額外紀錄每次join完後的首尾字母

所以我們定義: dfs(i, start, end) 返回 minimum concatenated length

那這樣的話上面兩種決策就能轉為
1. dfs(i+1, start, words[i][-1]) + (n-1 if end == words[i][0] else n)
2. dfs(i+1, words[i][0], end) + (n-1 if words[i][-1] == start else n)

**base case**

`if i == len(words): return 0`

那我們dfs從1開始: `dfs(1, words[0][0], words[0][-1])`

那最終答案就是`dfs(1, words[0][0], words[0][-1]) + len(words[0])`

time: O(n * 26 * 26)
space: O(n * 26 * 26)