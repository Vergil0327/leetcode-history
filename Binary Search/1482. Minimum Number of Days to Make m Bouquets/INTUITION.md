# Intuition

這題要求最少幾天可以完成，首先我們可以先判斷

如果總共花數小於 `m*k` 的話，那不管幾天都無法完成，可直接返回`-1`

但如果花數夠的話，那代表這題肯定有解
並且由於天數越多，花數越多，天數越少，開的花數越少，符合單調遞增的特性，因此我們可以嘗試看看能不能binary search

大體框架很簡單，search space從0天到全開，也就是`max(bloomDay)`

然後我們就二分搜值去猜開花的天數，然後判斷能不能湊齊到足夠的花數即可

```py
l, r = 0, max(bloomDay)
while l < r:
    mid = l + (r-l)//2
    if canMake(mid):
        r = mid
    else:
        l = mid+1
return l
```

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(1)$$