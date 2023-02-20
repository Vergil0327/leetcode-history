# Intuition

**操作1**

由於nums1[i]都是`0`或`1`，並且對nums1的更新就只會是flips 0 or 1
因此我們可以將nums1[i]轉為二進位制

這樣我們就可以用 `XOR` 來翻轉`0`、`1`

對於一段連續範圍的bits，我們可以用兩個bit mask來翻轉，例如:

```
1[010110]11
  b    a
0 111111 11 -> nums1 XOR this mask (mask2)
         11 -> nums1 XOR this mask (mask1)

1 101001 11 -> updated value -> our target
```

由於XOR兩次會回到自身，因此低位數的bits不變
而中間要更新的範圍可以跟`111...111`的bitmask相互XOR來翻轉

至於mask1跟mask2可以透過以下操作得到

```py
mask1 = (1<<a)-1
mask2 = (1<<(b+1))-1
```

因此我們的range update即為 `num1 ^ mask1 ^ mask2`

**操作2**

   nums2[i] = nums2[i] + nums1[i] * p
-> nums2[i] += nums1[i] * p
-> sum(nums2) += sum(nums1) * p

也就是說每當有type2的操作時，都是加上 `sum(nums1) * p`
由於nums1[i]只會是0或1，因此`sum(nums1) * p = count_one_bit(num1) * p`

由於每次都是總和相加，因此只要維護nums2的sum即可
所以我們用`nums2sum`來記錄每次sum(nums2)的變化

**操作3**

就是把sum(nums2)存到結果裡
