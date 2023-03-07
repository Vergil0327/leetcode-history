# Intuition

一開始是想到BFS，但對於10^6級別，嘗試後發現會TLE後嘗試用數學解

首先可以用`log(label)`時間找到目標`label`所處的row

```py
row = 1
while ((2**row)-1) < label:
    row += 1
```

然後我們從`label`這個node一路往回走，回溯到root，也就是`label=1`，並將一路上的node加進`path`裡，這樣最後把`path` array 倒轉即為答案

其中row從`1 ~ n`

我們可以這棵樹想成rows[i], BFS的概念
對於當前row來說，我們分奇數列跟偶數列討論:

1. 如果當前是偶數列
那麼最左邊節點的label `leftmost` 為`(2**row)-1`，同時也是該row最大的數

偶數列的label是由左往右遞減，所以此時`label`的index為`index = leftmost-label`

那麼`label`的父節點index即為該節點的`index//2`

透過父節點的index, 我們即可算出該父節點的label為:
`2**(row-2) + parentIdx`, 其中`2**(row-2)`為前一列的leftmost節點的label (因為奇數列是由左往右遞增)

2. 如果當前是奇數列

那麼最左邊節點的label `leftmost` 為`leftmost = 2**(row-1)`
但此時`label`的index為`index = label-leftmost`, 因為奇數列的最左側是該row的最小值

知道節點index後，父節點的index就等於`index//2`
所以父節點的label就等於`leftmost-1 - parentIdx`

透過這兩種情形，我們就能一路從label往回走回root