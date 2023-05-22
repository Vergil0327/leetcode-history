# Intuition

首先我們能想到的是越高位的1越多越好
那麼對於最高位來說:
如果grid[i][0]為**0**的話, 就算後面全都是**1**
把第一位翻轉成**0**後的值肯定比不翻轉來的大

```
0111111111...
1000000000...
```

所以首先我們先把最高位全不翻轉成**1**

```py
m, n = len(grid), len(grid[0])
for i in range(m):
    if grid[i][0] == 0:
        for j in range(n):
            grid[i][j] = 1-grid[i][j]
```

再來我們用個`cnt` array來紀錄每一個column的`1`的個數
因為我們是要求總和的最大值, 在固定最高位後
剩下的操作為了不翻轉到最高位
一定是逐個column來看, 只要每個column的`1`的個數**小於一半**, 我們便翻轉該column
這樣從最高位一路往低位翻轉, 最終的grid即為最大值

```py
cnt = [0] * n
cnt[0] = m

for j in range(1, n):
    for i in range(m):
        cnt[j] += grid[i][j]
    
    # flip if 1's count less than half
    if cnt[j] < m/2:
        cnt[j] = m-cnt[j]
```