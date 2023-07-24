
ax+by = 1 如果要有整數解, 那麼gcd(a,b)必須為1，兩者必須互質
ax + by + cz = 1也是一樣, gcd(a,b,c)必須為1

因為如果gcd(a,b,c) != 1, 代表:
ax+by+cz可以寫成 m * (a'x+b'y+c'z) where m is greatest common divisor

所以我們目的是找到一段subarray其中裡面的元素最後取gcd=1
因此我們只要挨個遍歷一遍維護gcd即可
只要最後gcd=1, 肯定存在一段subarray能包含互質的元素

```
    [12, 6, 7]
GCD  12, 6, 1
```