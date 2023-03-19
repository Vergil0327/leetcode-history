# Intuition

一開始的想法box從小到大優先放入，所以先找到從左邊開始跟右邊開始找出高度遞減的最深處
然後我們就能用two pointers從深處往外持續試著放box進去
```py
l, r = 0, len(warehouse)-1
        while l+1 < len(warehouse) and warehouse[l] >= warehouse[l+1]:
            l += 1
        while l < r and r-1 >= 0 and warehouse[r] >= warehouse[r-1]:
            r -= 1
```

但這樣其實不好處理，所以我們可以反向思考
我們就直接將box由大到小從兩側依序放入, 變成two pointers由外往內的形式
然後我們目的就是將box放在越適合的地方越好
所以有以下幾個條件:

1. 一但`l` > `r`, 代表warehouse已經沒有空間, 直接break
2. 一但box高度比兩側都還要高, 那就代表box已經無法放入, 直接跳過, 看下一個較小的箱子
3. 再來就是看`warehouse[l]`跟`warehouse[r]`哪個比較適合放box
   - 如果 `warehouse[r]`放不下，那只能放`warehouse[l]`
   - 如果兩邊都放得下，那就挑高度更小的warehouse優先放

所以本質是`Greedy + Two Pointers`