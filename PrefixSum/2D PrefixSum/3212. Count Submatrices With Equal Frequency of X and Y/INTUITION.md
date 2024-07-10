# Intuition

我們希望submatrix的"X", "Y"是**balanced**的, 所以能很直覺想到, 我們能這麼轉換
- "X" -> 1
- "Y" -> -1
- "." -> 無關緊要 -> 0

那這樣我們就能透過prefix sum來找出合法submatrix, 符合條件如下:
1. must contains 1 "X" at least
2. balanced

所以我們用2個2D prefix sum:
1. 紀錄submatrix的X個數
2. 紀錄submatrix的balance狀況

然後將所有合法submatrix個數加總即可