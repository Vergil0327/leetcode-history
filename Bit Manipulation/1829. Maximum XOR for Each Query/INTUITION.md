# Intuition

query1: XOR(X X X X X X X X Y) XOR k = x XOR k1
query2: XOR(X X X X X X X X)   XOR k = x XOR Y XOR k2

1. 首先XOR的特性, remove last element可以表示成 XOR(nums) XOR nums[-1]
2. 先看第一個query, 要使得answer1最大, k1必須是在maximumBit以內, 與XOR(nums)相互互補的bitmask
    - bitmask = (1<<maximumBit)-1
    - k1 = bitmask XOR (bitmask & XOR(nums))
    - ki = bitmask XOR (bitmask & (XOR(nums) XOR nums[n-i] for i in range [0,i]))
    - 大於maximumBit的部分則維持不變

所以我們XOR(nums)能分成:
1. 超出maximumBit的prefix
2. 在maximumBit內的suffix

```
{XXXX}{XXXXXXXX}
 pre      suf
```
我們不需要知道前半部分, 我們僅需要知道可進行操作的後半部分即可
那後半部分我們能用`bitmask = (1<<maximumBit)-1` 對`XOR(nums)`進行AND來得到
得到之後k = bitmask^suffix where suffix = bitmask & XOR(nums[:n-i])

time: O(n)
space: O(1)