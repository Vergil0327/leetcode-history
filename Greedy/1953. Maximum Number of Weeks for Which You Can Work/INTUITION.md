# Intuition

這題想到是優先作最多數目的project, 但卻想不到一個最佳的間隔方式來挑

但實際上我們要做的是, 我們有`n`種project, 我們要盡可能地將相同的project間隔開來
所以我們看最多數目的project有多少個

我們說每個種類的project, 最多有`max(milestones)`個

```
X X X X X X X X X X X X X X X X X
```

那如果這個project不超過總projects的一半, 代表我們可以在兩兩間隔中穿插其他種project
```
X O X O X O X O X O X Y X Y X Y X
```

這時我們所有project都可以做完

但如果某一種project超過總數的一半, `max(milestones) > total`
代表我們最多只能穿插`total - max(milestones)`這麼多個在間隔中

```
X X X X X X X X X |  X X X
 O O O O O O O O  |
```

所以我們最多只能做完`(total - max(milestones))*2+1`個