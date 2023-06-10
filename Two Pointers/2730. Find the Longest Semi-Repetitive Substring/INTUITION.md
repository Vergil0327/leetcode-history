# Intuition

數據規模很小, O(n^2)也能過
但實際上這題最佳解可以用雙指針解

```
s = XXXXXX 1 1 XXXXX 2 2 XXXXX
    l                  r ->
```

對於一個string來說, 我們可以用雙指針`l`跟`r`同時往右移動

對於一個`[l,r)`的雙指針來說, 框架為:
```py
n = len(s)
l = r = 0
while r < n:
    r += 1

    if l < r and pair > 1:
        # move `l`
```

每當有一個連續的pair, 亦即`if r-1>=0 and s[r] == s[r-1]`時
代表找到一個連續的pair, 此時`pair += 1`

那這時`l`該移動到哪? 由於連續pair不得超過1個
所以由上面例子來看, `l`應當移動到前一個pair的位置（如下圖所示)
然後右指針`r`繼續往右移動

```
s = XXXXXX 1 1 XXXXX 2 2 XXXXX
    l                  r ->

s = XXXXXX 1 1 XXXXX 2 2 XXXXX
             l         r ->
```

由於我們要依序並持續紀錄當前與前一個consecutive pair的index
所以我們直接用個`stack`來存index
一但`pair > 1`, 便將`l`移動到`pairIdx[-2]`, 也就是前一個consecutive pair的位置
```py
if l < r and pair > 1:
    l = pairIdx[-2]
```