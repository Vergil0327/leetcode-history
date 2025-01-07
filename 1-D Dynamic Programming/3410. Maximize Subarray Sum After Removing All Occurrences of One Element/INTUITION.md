# Intuition

```
X X X X {X O X O O X X X X O X O X}
         l                       r
```

理論上一段subarray sum, 可以選擇一個nums[i]刪除, 肯定是選一個貢獻度最高了
subarray sum又可以用兩段prefix sum來表示

```
max subarray sum = prefix_sum[r] - prefix_sum[l-1] - deletion_sum[l:r], 其中deletion_sum[l:r] = # of x in array[l:r] * x
```

所以首先比較簡單的是維護prefix_sum[r], prefix_sum[l-1]
為了讓subarray sum最大化, 那麼我們得持續對prefix_sum[l-1]取`min()`

```py
res = -inf
presum_r = presum_l = 0

for x in nums:
    presum_r += x
    presum_l = min(presum_l, presum_r)
```

再來得找出最值得消除的`x`, 這邊我們可以用hashmap去紀錄每個x的出現總和
但對於當前想消除的`x`來說, 他除了可以基於先前的所有`x`以外, 也可以基於先前最小的presum_l


```
O O O O O O O O O O X

_sum = Counter()
for x in nums:
    _sum[x] = min(_sum[x], presum_l) + x
```

那這樣該有的資訊就都有了, 對於當前的subarray sum來說, 最好的deletion sum就是

```py
deletion_sum = 0 # initial value

# ...

deletion_sum = min(deletion_sum, presum_l, _sum[x])
```

綜合上述, 最終就是: `res = max(res, presum_r - deletion_sum)`

```py
res = -inf
presum_r = presum_l = deletion_sum = 0
_sum = Counter()
for x in nums:
    presum_r += x

    res = max(res, presum_r - deletion_sum)

    _sum[x] = min(_sum[x], presum_l) + x # 這邊注意順序, 不能讓presum_l先被更新
    presum_l = min(presum_l, presum_r)

    deletion_sum = min(deletion_sum, presum_l, _sum[x])
return res
```

整體來說, 有點像是kadane algorithm
每次都基於新的立足點`x`來更新最小subarray sum
然後得出我們整段prefix sum扣掉負數subarray sum後所能得到的最大值