# Intuition

## Brute Force - knapsack problem

每行選一個，我們把當前第`i`行的所有可能的sum都儲存起來
這樣下一行在選的時候，就只可能從前一輪的所有可能的sum轉換過來

所以第一行選完有 `len(mat[0])` 種可能
第二行在選，就會有 `len(mat[0])` * `len(mat[0])` 種可能
所以種共會有 m^n 種可能的選擇

但如果我們轉換成記錄他們的sum的話，其實這`m^n`種可能選擇的sum會有大量重複
這樣會大大減少時間複雜度

以example 1為例:

[[1,2,3],[4,5,6],[7,8,9]]

第一輪sum: 1, 2, 3
第二輪sum: 5,6,7  6,7,8  7,8,9 -> 去除重複後變為 -> 5,6,7,8,9
第三輪sum: 12,13,14,15,16  13,14,15,16,17  14,15,16,17,18 ->  12,13,14,15,16,17,18
實際上3*3*3種可能選擇中，他們的sum僅有7種

而這其實就是背包問題，每一row都是從前一個背包的物品中裝到當前這個背包中後，在加上當前可以選擇的物品

>背包問題實際上也是暴力搜索，遍歷所有物品可能
>只是它記錄的是容量而不是選擇，所以在所有可能容量中可能會出現重複而大大透過dp table而降低時間複雜度

所以我們可以用一個集合hashset來作為背包，每一輪選擇都只跟前一輪相關
所以我們用兩個集合就可以了

一開始**base case**:

`dp = {0}` -> 總和為0

**狀態轉移**

當前狀態就是當前可以選擇的可能性加上前一輪的總和

```py
for i in range(ROWS):
    nxt = set()
    for _sum in dp:
        for v in mat[i]:
            nxt.add(_sum+v)
    dp = nxt
```

最後答案就找與target最接近的sum即可

```py
min(abs(_sum-target) for _sum in dp)
```

## Further Optimized

這邊有個能做的optimization是

由於我們是要求出`與target絕對值最小的值`
所以對於所有dp內所有大於target的總和當中，其實我們只要留與target最近的就好

所以我們可以多個`if-else`判斷

如果前一輪總和加上當前的值仍**小於target**，那就加入到集合當中
如果前一輪總和加上當前的值**大於target**，那我們就先記錄下來，然後取最小的加入到集合當中
把所有超出target的可能狀態壓縮成一個，這樣可大幅降低時間複雜度

```py
greaterThanTarget = inf
for v in mat[i]:
    if _sum+v <= target:
        nxt.add(_sum+v)
    else:
        greaterThanTarget = min(greaterThanTarget, _sum+v)
if greaterThanTarget != inf:
    nxt.add(greaterThanTarget)
```