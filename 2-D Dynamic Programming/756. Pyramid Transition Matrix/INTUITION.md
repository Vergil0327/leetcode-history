# Intuition

```
allow pattern:
allowed => allowed[:2] -> allowed[2] where allowed[:2] as bottom and allowed[2] as top
```

`n = len(bottom) => means totally n level`

由下往上, 下一個level會依據當前的level作為bottom而有所限制, 選擇只能從allowed pattern裡面選
下個狀態只跟前一個狀態有關, 所以目前想到的是用dp來解

那對於當前level來說, 第i個letter取決於前一個level的(i, i+1)個作為bottom並且必須是allowed pattern
所以我們可以從第一層開始, 然後嘗試所有可能allowed pattern看最後能不能組成bottom

```py
# dp[level][i], dp[level][i+1] -> dp[level-1][i]
# dp[level][i]: the valid letters at i position of the level
for level in range(n-1, 0, -1):
    for i in range(level-1):
        for left in dp[level][i]:
            for right in dp[level][i+1]:
                if (bot := left+right) in pattern:
                    dp[level-1][i] += pattern[bot]
return dp[1][0] != ""
```

但這樣其實是有誤的, 如果i=0時, `bottom = left+right`決定後, 下個i=1位置left'就會限制`left'=right`
所以每一層遍歷完後, 只會建構出下層唯一的bottom string
而不像上面那樣可以任意組合

所以比較直覺的想法應該是從n level的bottom開始,其中`i from 0 to n-1`透過dfs與allowed嘗試建構出下個level的bottom string
然後最後判斷能不能構造出長度為1, 也就是level=1的bottom string