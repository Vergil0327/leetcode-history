# Intuition

仔細觀察其實good split的重點在於兩個`1`中間有多少個`0`


我們重點是分出每個區間總和為1

```
[10000]100...
```
所以看上面, 對於`10000`來說
我們可以這麼分:
1. 1|0000100
2. 10|000100
3. 100|00100
4. 1000|0100
5. 10000|100

我們總共有4個0加上自身1, 共有5個split的位置
所以我們可以看成多個`1000`subarray:
`[1000..][1000...]`
而方法數會是每個subarray的split選擇相乘, 是乘法原理

1. 所以首先我們先移除leading zeros
2. 然後看有多少個[1000...]subarray, 把他們方法數相乘最後對10^9+7取餘數即可

**edge case**
有一點要注意是: suffix zeros也是沒有用的
所以必須:
```py
while j < n and nums[j] == 0:
    j += 1
split = (j-(i+1))+1
if j < n and nums[j] == 1:
    res *= split
```

ex. [1000]
依我們的計算, split選擇應該有4種
但由於後面沒有good subarray split, 後面都是suffix zeros
所以實際上只有一種方法選擇, 就是`1000`