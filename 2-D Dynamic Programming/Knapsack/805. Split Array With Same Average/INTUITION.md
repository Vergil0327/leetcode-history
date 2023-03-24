# DFS 搜索

## Intuition

nums = [X X X X X X X X] {X X X X X}
               A             B
SUM = sum(nums)
sumA / nA = (SUM-sumA) / (n-nA)

首先透過可選可不選的策略, 透過兩個non empty subset的average判斷
可以很快地寫出最基本的DFS

但這樣時間複雜度會有點高，給使透過bitmask也是如此 TO(2^n)

但實際上我們可以在推導一下關係式, A, B兩個avg相等時
代表整個nums的平均也相等

sumA / nA = (SUM-sumA) / (n-nA) = SUM / n
=> sumA * n = SUM * nA

因此推導一下後可以得出`sumA * n = SUM * nA`
透過此條件的約束可發現:
`size * SUM // n = sumA`, 代表`size * SUM % n`餘數必須為零
加上這個條件後，在進行DFS搜索前可以進行大量剪枝
汰除掉不合理的組合, 僅對可能組合進行DFS來判斷可不可行

我們對 sumA 進行搜索, 如果存在，那代表可以成功分成兩個平均相等的subset
```py
for size in range(1, n):
    if size * SUM % n != 0: continue
    sumA = size * SUM // n
    if dfs(0, sumA, size): return True
```
