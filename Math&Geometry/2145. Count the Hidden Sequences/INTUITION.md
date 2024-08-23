# Intuition

brute force solution

```py
n = len(diff)

res = 0
for first in range(lower, upper+1):
    num = first
    valid = True
    for d in diff:
        num += d
        if num < lower or num > upper:
            valid = False
            break
    res += int(valid)
return res
```

再來想法是我們去找出max_delta跟min_delta, 分別為`mx`, `mn`
那麼我們就知道我們數值的範圍為 **[mn,mx]** 而這個範圍內必須落在 **[lower,upper]**

```py
n = len(diff)

delta = mx = mn = 0
for d in diff:
    delta += d
    mx = max(mx, delta)
    mn = min(mn, delta)

if upper-lower < mx-mn: return 0
```

因此, 這時有解的情況為: upper-lower >= mx-mn
無解情況為: upper-lower < mx-mn

- if upper-lower < mx-mn: return 0
- if upper-lower == mx-mn: return 1
- 再來討論upper-lower > mx-mn的情況

```
[lower X  X  X  X  X  X  upper]
  mn   X  X  X  mx
       mn X  X  X  mx
          mn X  X  X  mx
             mn X  X  X  mx
                mn X  X  X  mx => X (out-of-bounds)
```

如圖所示, 合法解的數目為: `(upper-lower+1) - (mx-mn+1) + 1`