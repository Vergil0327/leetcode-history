# Intuition

先想brute force

只有5*2會產生10導致trailing zero產生, 所以先找出[left,right]內的所有(2x5) pair
接下來剩下的就不會再產生trailing zero, 我們再來處理<pre> <suf>的部分

扣掉(2x5) pair後的所有因數相乘, 即能找出<pre> <suf>

```py
factors = defaultdict(int)

for num in range(left, right+1):
    for i in range(2, int(sqrt(num))+1):
        while num%i == 0:
            num //= i
            factors[i] += 1
    if num > 1:
        factors[num] += 1
C = min(factors[2], factors[5])
factors[2] -= C
if factors[2] == 0:
    del factors[2]
factors[5] -= C
if factors[5] == 0:
    del factors[5]

res = 1
for v, freq in factors.items():
    res *= pow(v, freq)
pre, suf = deque(), deque()
while res:
    d = res%10
    res //= 10
    if len(suf) < 5:
        suf.appendleft(d)
    else:
        pre.appendleft(d)
        if len(pre) > 5:
            pre.pop()
```

由於res會非常大, 會大到超出string conversion的限制導致發生錯誤: **Exceeds the limit (4300 digits) for integer string conversion**
因此比起全轉為string, 我們必須用其他方式來取出前5跟後5個digit

以上是TLE version, 會敗於test case: left=123, right=9789

前面取factor為n * sqrt(n) ~ 10^6 => 是合理的time complexity
但最後res可能會高達3萬多位數, 這麼大的數要找出前5跟後5 digits的計算太耗時間
所以可能要想其他方式去找

改成在乘積的過程中, 分別維護pre, suf, trailing_zeros

trailing_zeros 跟 suf是一組的
我們可以乘積過程中持續判斷有沒有產生trainling zero: `suf%10 == 0`, 有的話就`suf//0 and trailing_zeros += 1`
然後關於suf, 我們也不用紀錄全部位數, 我們就用pow(10, 6)來取餘, 最後再取出last 5 digits即可
但注意這邊必須是移走trailing zeros後的last 5 digits, 所以先移走trailing zeros然後再對pow(10, 6)取餘
而且為啥是pow(10, 6)?
因為如果suf保留的太少, ex. suf = XXX102345, 只取1e5會把leading zero給省略掉

註: 但後來發現在test case: left=6365, right=8375下, suf對pow(10, 6)取餘也是不夠的
所以乾脆pre也跟suf都一樣pow(10, 16)取餘

所以關於suf跟trailing_zeros:
```py
suf = 1
zeros = 0
mod = pow(10, 7)
for num in range(left, right+1):
    suf *= num
    while suf%10 == 0:
        suf //= 10
        zeros += 1

    suf %= mod
suf = str(suf)[-5:]
```

那麼pre該怎麼取?

相乘到最後會類似像這樣: num = X X X X X X ... suf 0 0 0 0 0 0 0 0 0 0
所以我們pre一樣持續進行乘積, 然後移除trailing zeros, 每移除一位就紀錄位數+1

然後如果數值`num`夠大, 那麼乘積就幾乎不會影響到前面位數, 至於要多大可能要試一下
我們就取個15位數好了, 前5位是我們要的, 試試保留後面十位數看看精度夠不夠
也就是: `if pre >= 1e16: pre //= 10`

```py
for num in range(left, right+1):
    pre *= num
    while pre%10 == 0:
        pre //= 10
        total_digits += 1

    while pre >= mod:
        pre //= 10
        total_digits += 1
```

那最終答案就可以寫成:

```py
suf = str(suf)[-5:]
pre = str(pre)

digit_len = total_digits + len(pre) - zeros

# 取不包含suf的前五位
pre = pre[:min(5, max(0, total_digits-zeros-5))]

if digit_len <= 5:
    return f"{suf}e{zeros}"
elif digit_len <= 10:
    return f"{pre}{suf}e{zeros}"
else:
    return f"{pre}...{suf}e{zeros}"
```

這題就是純粹的數學, 重點在於取餘求suf以及捨棄一定位數以上的精度取pre