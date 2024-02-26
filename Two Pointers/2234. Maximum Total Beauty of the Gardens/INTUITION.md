# Intuition

flowers[i]: X X X X X X X X X X X X
flowers[i] >= target: complete
flowers[i] < target: incomplete

beauty = # of flowers[i] >= target * full + min(incomplete) * partial

## observation

flowers[i] 只要滿足 >= target後, 種更多也不會增加beauty, 所以要增加的話最理想情況就是種到 >= target即可

直覺想到newFlowers如果要加到garden讓他complete, 肯定是先加到較大的那個
所以一開始先想到可以對flowers由大到小排序

由於beauty = k*full + max_incomplete*partial, 其中k跟max_incomplete是變數
我們可以嘗試遍歷所有可能`k`, 然後求出max_incomplete, 找出全局最優解

當complete garden有k個時, 此時的分數至少為`k*full`
這時我們就來找max_incomplete

我們手中有newFlowers可運用來拉抬max(min(flowers[k:]))
如果flowers[k]*(n-k) < newFlowers + sufsum[k] where sufsum is sum(flowers[k:])的話
代表我們可以透過newFlowers將後面整個suffix sum補齊, 使得max_incomplete = flowers[k]
但如果不行的話, 指針就樣往右移

所以我們這邊改成用另一個index `j`表示
```py
j = max(j, k)
while j < n and (sufsum[j]+newFlowers) < flowers[j] * (n-j):
    j += 1
```

由於complete garden越來越多, newFlowers會持續將flowers[k]補到target使其complete
因此newFlowers會越來越少, 這時會發現`j`會是單調往右走
所以這邊會是個雙指針, `k`, `j`同步往右, 分別代表complete, incomplete的資訊

那等到`j`停下來後, 我們可以很簡單的算出:
`max_incomplete = (sufsum[j]+newFlowers) // (n-j) if j<n else 0`

那這邊要注意, max_incomplete有個上限是最多到`target-1`, 所以:
```py
beauty = k*full
if j < n and flowers[j] < target:
    beauty += min(max_incomplete, target-1) * partial

res = max(res, beauty)
```

等到該輪結束後, 下輪有`k+1`個garden, 代表flowers[k]必須至少為target
我們必須計算一下, 如果flowers[k] < target, 我們必須拿newFlowers去補
一但newFlowers不夠了, 代表我們湊不出`k+1`個complete garden, 因此我們就break-loop

```py
if n > k >= 0 and (diff := target-flowers[k]) > 0:
    newFlowers -= diff
if newFlowers < 0: break
```