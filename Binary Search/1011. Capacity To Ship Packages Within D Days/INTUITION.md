# Intuition

這題要找一個最低的capicity使得我們能在`days`內全部運輸玩，並且只能從一端開始接續往右陸續運輸

capacity越大，所需天數越低，反之則需要越多天
很明顯存在著一個極值，因此我們可以試著用binary search來猜猜看這個capacity

基本框架就是

```py
l, r = 0, sum(weights)
while l < r:
    mid = l + (r-l)//2
    if self.canShip(mid, weights, days):
        r = mid
    else:
        l = mid+1
return l
```

只要可以在天數內運輸，代表我們猜的`mid`可能是個解，但還可以往下猜猜看，因此`r = mid`
反之如果不行，就拉高下限，`l = mid+1`

那這個canShip要檢查的是:

我們整個遍歷一遍，如果超出capacity那剩下的就只能隔天再繼續，因此
```py
carry = day = 0
for w in weights:
    if carry+w>cap:
        day+=1
        carry = 0
    carry += w
```

別忘了如果我們的capacity小於任何一個weights[i]的話，我們將無法運輸，因此我們還得判斷:
`if weights[i] > cap: return False`

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(1)$$