# Intuition

效率最高的堆疊方式

俯視圖, 數字代表高度
```
1

21
1

321
21
1

4321
321
21
1

如果側視來看
最右層放1個
左一層放2+1個
再左一層放3+2+1個
最左層放4+3+2+1個
總堆疊個數為1 + (1+2) + (1+2+3) + (1+2+3+4)
所以如果得出為layer = [4,3,2,1], 那麼總堆疊個數就是他的sum(suffix_sum[y] for y in range(height, -1, -1)) 

再看個例子
n為上面例子再多1, 那麼額外這個箱子就必須在最下層往外放

4321
321
21
1
1

側視就相當於
5321
321
21
1
以最左那行來看, 最底層多疊一個箱子, 最下層有5個箱子
上面則沒變, 由下往上箱子一樣3 -> 2 -> 1
```

如果已知最下面一層的三角形面積為 area = (1 + d) * d // 2
=> (1+d)*d = 2*area => d^2 + d - 2*area = 0
=> ax^2+bx+c = 0  => x = (-b +/- sqrt(b^2-4ac))/2a
=> d = floor((-1 + sqrt(1 + 4 * 2*area))/2) => 完整的三角形
=> 那麼area - (1+d)*d/2就會是多出來的零頭, 再把零頭往最底層的每一行一個一個加上去

```py
remain = area - (1+d)*d//2

rows = [0] * d
for i in range(d):
    rows[i] = d-i
for i in range(diff):
    rows[i] += 1
```

這樣就能知道當前area能疊幾個箱子
```py
total = sufsum = 0
for i in range(d-1, -1, -1):
    sufsum += rows[i]
    total += sufsum
return total
```

所以可以用binary search去猜測area, 然後求出d跟total, 然後比較total有沒有 == n
如果total >= n, 那當前area可能為解, 縮小上界
如果total < n, 代表猜小了, 拉高下界

```py
l, r = 1, int(1e9) # area: 1 <= n <= 10^9
while l < r:
    area = l + (r-l)//2
    if cal(area) >= n:
        r = area
    else:
        l = area+1
return l
```
