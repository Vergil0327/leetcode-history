# Intuition

首先想的是二維prefix sum:

我們想成能蓋印章的位置為1的話, 那麼:
`area = presum[i][j] - presum[i][j-stampWidth] - presum[i-stampHeight][j] + presum[i-stampHeight][j-stampWidth]`
這樣的話, 如果 area == stampHeight * stampWidth, 代表我們能蓋印帳在這塊area上, 其中grid[i][j] is bottom-right position of stamp

所以我們能找出所有能蓋印章的右下位置
ex. stamp = 4x3
```
X _ _ _
X _ _ _
X _ _ _
X _ _ 1
```

如果底下再多一row
```
X _ _ _
X _ _ _
X _ _ _
X _ _ 1
X _ _ 1
```

如果右邊再多一column
```
X _ _ _ _
X _ _ _ _
X _ _ _ _
X _ _ 1 1
X _ _ 1 1
```

這些標記為1的地方都是能蓋印章的合法右下位置, 也代表從那位置往回stampWidth, stampHeight的範圍都囊括進來了

所以如果我們標記出這些位置後, 我們再次遍歷所有grid[i][j] == 0的位置, 我們只要確認這位置的整個右下區塊有沒有合法的印章能囊括他

引此我們再透過一個prefix sum (1-indexed)來算出這些合法印章的數量, 我們就能透過這個presum來看:

```
if grid[i][j] == 0:
    numStamp = presum2[min(i+stampHeight, m)][min(j+stampWidth, n)] - presum2[i][min(j+stampWidth, n)] - presum2[min(i+stampHeight, m)][j] + presum2[i][j]
    if numStamp > 0:
        grid[i][j] 被至少一個印章給蓋到
    else:
        grid[i][j] 沒被任何印章給蓋到 => 直接返回False
```