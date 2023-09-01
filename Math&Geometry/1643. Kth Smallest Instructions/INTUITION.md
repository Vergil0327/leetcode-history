# Intuition

我們需要
destination[0] 個 "V"
destination[1] 個 "H"

我們需要的是第k個字典序排列, 其中"H" < "V"
所以第一個最小字典序一定是: `s = "H" * destination[1] + "V" * destination[0]`

一開始想法是:
```py
for _ in range(k-1):
    s = nextPermutation(s)
return s
```

至於nextPermutation
以"HHHVV"為例:
"HHHVV" -> "HHVHV" -> "HHVVH" -> "HVHHV" -> "HVHVH" -> "HVVHH" -> "VHHHV" -> "VHHVH" -> "VHVHH" -> "VVHHH"

1. 由後往前找, 跳過字母順序已經正確的部分後, 找出s[i] < s[i+1]的地方後, 會找出s[i]是需要swap的地方
2. j再由後往前找, 找出第一個比i大的位置後兩個swap. arr[i], arr[j] = arr[j], arr[i]
3. 將s[i+1:]後面進行排序, 形成最小字典序.
ex "HHHVV" -> swap -> "HHVHV", then "HHVHV" -> sort -> "HHVHV"
ex. "HHVHV" -> swap -> "HHVVH", then "HHVVH" -> sort -> "HHVVH"
ex. "HHVVH" -> swap -> "HVHVH", then "HVHVH" -> sort -> "HVHHV"
4. 其實就是leetcode 經典題目 31.

但會發現1 <= k <= nCr(row + column, row) where 1 <= row, column <= 15
k會到很大而導致TLE, 所以得改個方式來想

借用數學的組合數概念:
HHHVV

H**** => 如果確定第一位是H, 那麼後面有C(4,2)種可能 = 4 * 3 / (2 * 1) = 6
V**** => 由上面結果可知, 第一位如果是V, 那麼至少是第6個以後的排列
確定是H或V後, # of H 或 # of V數量就`-= 1`

如果k比6大, 那就`k -= 6`, 且該位確定為"V", 然後再繼續往下一位找
如果k<=6, 代表第一位是H, 然後再看後面四位, 如果第一位是H
HH*** or VH*** => 有C(3, # of V) = C(3,2) = 3
如果k比3大, 那麼第二位就為"V", 不然則為"H"

直到k為0
途中如果V或H的數目用完了, 那就代表確定完位置了, 把剩下的"V"或"H"加上string即可