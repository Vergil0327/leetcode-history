# Intuition

遍歷所有substr的話會是$O(n^2)$, 這肯定是會TLE的
所以這類型的題目其實我們可以character by character的來想
來看每個s[i]能貢獻給多少substr, 最後全部加總即為答案

那接下來我們來看如果s[i] = X的情況會是怎樣


```
s = X [Y Y Y Y Y Y Y Y] X [Y Y Y Y Y Y Y Y Y] X
       l                i                  r 
            left                right
```

對於character `X`來說, 他能貢獻的substr只有在substr只有一個X的情況的時候, 這代表
- 左邊界`l`能延展至index of last occurence + 1
- 右邊界`r`能延展至index of next occurence - 1
- 那`X`的貢獻即為兩邊個數相乘 = left * right

所以我們只要知道每個s[i]的last occurence的index以及next occurence的index的話
我們就能計算出:
- left = i - lastCharIdx[s[i]]
- right = nextCharIdx[s[i]] - i
- 所以 res += left * right

對於lastCharIdx:
- 初始為一個[-1] * 26的array
  - 因為總共就26個大寫字母
  - `-1`是考慮到如果`l`, `r`兩邊界都可以是`i`本身. 亦即`left`跟`right`都`>= 1`
- 每次計算完後都記得更新`lastCharIdx[s[i]] = i`

至於nextCharIdx:
- 初始化nextCharIdx[i][ch]的array, 代表在index==i且s[i] == ch時, index of next occurence = nextCharIdx[i][ch]
- 我們可以從後往前遍歷(26N)
  - 如果s[i] == ch, 紀錄`nextCharIdx[i-1][s[i]] = i`
  - 如果s[i] != ch, `nextCharIdx[i-1][ch] = nextCharIdx[i][ch]`

