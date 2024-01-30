# Intuition

觀察一下, 先把box翻轉成我們要的模樣

```py
m, n = len(box), len(box[0])
rotate = [[""]*m for _ in range(n)]
for i in range(m-1, -1, -1):
    for j in range(n):
        rotate[j][m-1-i] = box[i][j]
```

再來我們就從底部往上, 以obstacle `*`區分出間隔
記住一開始的位置, 然後持續計算每一段間隔有多少石頭
然後再從一開始往上填石頭`"#"`回去

相當於雙指針由底部往上, 一個指針先行計算區間有多少石頭, 並同時把走過的路都翻成empty `"."`
走到底後另一個指針在看有多少石頭, 一路填石頭`"#"`回去

time: O(m*n)
