# Intuition

因為有兩種方法可以搭乘，所以我們得記錄下來，因此我們這樣定義dp

```
dpReg[i] the minimum cost to reach stop[i] from stop 0 ended with regular route. (1-indexed)

dpExp[i] the minimum cost to reach stop[i] from stop 0 ended with express route. (1-indexed)
```

再來我們就看我們從前一站到下一站有哪些選擇

1. 如果我們搭乘regular抵達第`i`站，我可以從regular前一站搭來，或是從express到第`i`站，然後再轉乘過來，由於轉乘沒有cost，所以是:

    `dpReg[i] = min(dpReg[i-1] + regular[i], dpExp[i-1] + regular[i])`

2. 如果我們搭乘express抵達第`i`站，我們可以從前一站regular轉乘express然後再搭過來，或是從前一站的express搭過來，有這兩種狀態轉移:

    `dpExp[i] = min(dpReg[i-1] + expressCost + express[i], dpExp[i-1] + express[i])`

因此每一站的最佳解就是兩者取最小
```py
dpReg[i] = min(dpReg[i-1] + regular[i], dpExp[i-1] + regular[i])

dpExp[i] = min(dpReg[i-1] + expressCost + express[i], dpExp[i-1] + express[i])

res[i] = min(dpReg[i], dpExp[i])
```

**Base Case**

我們需要定義`dpReg[0]`跟`dpExp[0]`

一開始就在regular route，所以cost為0
`dpReg[0] = 0`

如果第0站要透過express抵達，那麼cost為expressCost
`dpExp[0] = expressCost`