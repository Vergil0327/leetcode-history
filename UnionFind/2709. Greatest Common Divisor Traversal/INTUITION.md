# Intuition

觀察三個example後會發現GCD > 1代表兩者之間有公因數存在
=> 有相同公因數的nums[i]跟nums[j]會因為共同因數而可以互相抵達
=> 想成是graph的話, 因數(factor)就相當於edge

那這樣的話其實我們就找出每個數的質因數即可

```
4    3   12      8
2*2  3   3*2*2   2*2*2
- 3是質數沒跟任何人連在一起
- 4跟2連在一起
- 12跟3還有2連接在一起
- 8跟2連接在一起
```

所以概念上就是我們找出每個數的因數, 然後將nums[i]跟他的因數union在一起
那這樣最後如果全部nums[i]都union在一塊, 就代表全部pair都可以相互抵達

所以首先先找出所有可能質因數
`nums[i]`數值的範圍是10^5, 所以實際上我們僅需要找到sqrt(10^5)範圍內的所有質數就好

因為後續我們對每個`nums[i]`做因式分解時, 也只會用到`sqrt(nums[i])`範圍內的所有質因數
因為nums[i]分解因數到最後, 不是剩下1就是剩下大於`sqrt(nums[i])`的質因數

例如: nums[i] = 6, factors = [2] -> 6 = 2*3

```py
factors = []
cur = nums[i]
for p in primes:
    if cur%p != 0: continue

    factors.append(p)
    while cur%p == 0:
        cur //= p
if cur != 1:
    factors.append(cur)
```

基於以上想法, 我們要做的是:

1. 首先所以質數可以透過**Sieve of Eratosthenes**來全部找出
2. 再來就找每個nums[i]的因數, 這些因數就相當於連接著nums[i]的edge
3. 把每個nums[i]都跟自己的因數union起來
4. 最後判斷每個數是不是全部union在一塊, 如果是那代表每個nums[i]都屬於同一個connected component