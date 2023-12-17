# Intuition

重點是差值, 所以一開始想到既然排序沒有影響
那就看看排序後有沒有什麼好處
```py
nums.sort()
```

[X X X X X X X X X X] X X X X X
觀察一下會發現其實這個subarray.length會受限於`k`
有種sliding window的感覺, 可惜當下contest沒想到

但實際上要將這個sliding window裡的每個數全部轉成Y, 且`sum(diff) <= k`的話
由於我們已經排序過, 最佳情況一定是將中位數前後的數透過操作往中位數靠
也就是以中位數作為中間, 後半段的sum(subarray[mid:])跟sum(subarray[:mid])相減必須小於等於k

所以我們可以用`sum(subarray[mid:])-sum(subarray[:mid]) <= k`作為條件來維護這個sliding window

最後就能用O(n)時間求出最大長度