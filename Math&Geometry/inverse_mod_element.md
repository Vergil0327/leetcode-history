
`x / a ≡ x * b (mod M)`

如果在**M是質數**的情況下, 上面式子由於左右兩式同餘

可以視為 `b = 1/a = inv(a)`

所以一般在有除法的情況下取餘數時, 除法是沒有餘數的相關定理的
但如果M是質數, 我們就可以預先處理inv_x = inv(x) = 1/x % mod

其中inv(x)可以這麼計算

1. 費馬小定理

```
inv(a) ≡ a ^ (M-2)  (mod M)
```

也就是:

```py
inv_a = pow(a, mod-2, mod)
```

2. 線性提早求出[1,n]的所有inverse element

```py
inv = [0] * N
inv[1] = 1

for i in range(2, N):
    inv[i] = (mod - mod//i) * inv[mod%i] % mod
```

3. 函式計算

```py
def inv(x: int):
    s = 1
    while x > 1:
        s = s * (mod - mod//x) % mod
        x = mod%x
    return s
```
