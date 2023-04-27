# Intuition

遍歷所有substring會是O(N^2), 如果我們能有一個比較高效率的判斷方式
能快速判斷當前的substring是不是echo string的話, 我們便能暴力搜索所有substring

```
X X X X X X X X X X
        i       j
```

我們把它想成雙序列DP, 然後這麼定義dp[i][j]
dp[i][j] = length which makes text[i+1-dp[i][j]:i+1] == text[j+1-dp[i][j]:j+1]

dp[i][j]為以text[i]結尾跟以text[j]結尾的最長公共長度

ex. if dp[i][j] == 3: 
```
X X [Y Y Y] X [Y Y Y] X
         i         j
```

而狀態轉移也很簡單, 我們只要考慮text[i]跟text[j]有沒有相等就好
- if text[i] == text[j], dp[i][j] = dp[i-1][j-1] + 1

```py
for i in range(n):
    for j in range(i+1, n):
        if text[i] == text[j]:
            if i-1 >= 0:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = 1
```

當我們知道dp[i][j]後
這樣一來如果dp[i][j] >= j-i的話, 代表text[i+1:j] (both inclusive)可以組成echo substring, 如下所示:

```
X X [Y Y Y] [Y Y Y]
         i       j

X [Y Y Y {Y] Y Y Y}
          i      j
```

所以一但`if dp[i][j] >= j-i`, 我們便可以把`text[i+1:j+1]`加入到**hashset**裡
最終答案就是**hashset**的大小, 或者我們可以同步用個變數記錄該**hashset**的大小

```py
res = 0
SET = set()
for i in range(n):
    for j in range(i+1, n):
        if dp[i][j] >= j-i: # which means text[i-dp[i][j]+1:i+1] == text[i+1:j+1]
            if text[i+1:j+1] not in SET:
                SET.add(text[i+1:j+1])
                res += 1
```