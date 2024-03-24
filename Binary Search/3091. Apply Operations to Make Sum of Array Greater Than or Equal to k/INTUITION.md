# Intuition

本題題意是:
increment `a` times to `a + 1`,
and then copy `b` times such that (a + 1) * (b + 1) >= k.

然後我們要找min(a + b) such that (a + 1) * (b + 1) >= k.

一開始先想說能不能用binary search去猜這個數, 如果`mid`次不行, 那`mid-1`肯定也不行
所以如果用binary search的話, 我們就只需要驗證`mid`次可不可行
問題就從找出合法解轉為找出可行解

那麼找minimum的binary search框架如下：
要讓`sum >= k`, 最多就是不用複製, 那就是k次
所以search space [l,r] = [0,k]

```py
l, r = 0, k
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l
```

現在重點就在於helper func `check`該怎麼檢驗

要讓`sum >= k`, 最多就是不用複製, 那就是k次
如果我們有先用增加, 然後再複製翻倍肯定會更快的

既然我們不確定我們應該先加幾次然後再複製, 所以我們全都試過一遍看可不可行即可

```py
def check(mid):
    for i in range(mid+1):
        # 進行 += 1 i次
        # mid-i次複製後, 總共會有mid-i+1個數
        if (1+i) * (mid-i+1) >= k: return True
    return False
```

time: O(klogk)

# Intuition 2 - Math

但其實這題能用數學解達到O(1)

繼續從`min(a + b) such that (a + 1) * (b + 1) >= k`這行做延伸

a+b是我們的操作次數, 如果令 v = a+b
那對於相同的操作次數`v`來說, (a + 1) * (b + 1)的值最大的情況發生在a+1 == b+1
也就是a=b的情況

所以我們可以先找出`v = sqrt(k)`, 這個v就是滿足v*v >= k的最小數
由於我們只可能是正整數, 所以v = ceil(sqrt(k))

那麼increase次數: a = v-1
而複製次數則為: k // v - (k % v == 0) (剛好整除的話就不用再複製那一次了)

```py
v = ceil(sqrt(k))
return v - 1 + k // v - (k % v == 0)
```