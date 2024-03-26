# Intuition

example 2:
prevRoom = [-1,0,0,1,2]
index    = [ 0,1,2,3,4]

```
decision tree:
0 -> [1,2] -> 1 -> [2,3] -> 2 -> [3,4] -> 3 -> [4]: 0,1,2,3,4 
                                       -> 4 -> [3]: 0,1,2,4,3
                         -> 3 -> [2] -> 2 -> [4]  : 0,1,3,2,4
           -> 2 -> [1,4] -> 1 -> [3,4] -> 3 -> [4]: 0,2,1,3,4
                                       -> 4 -> [3]: 0,2,1,4,3
                         -> 4 -> [1] -> [3]       : 0,2,4,1,3
```

該怎麼模擬這個decision tree?

dfs(i): the number of ways to build
dfs(0) = dfs(1) * dfs(2) * 這兩種分支的排列方式
那現在就變成**"這兩種分支的排列方式"**該怎麼求得?

假設以1為節點這個subtree有x個節點
以2為節點的subtree有y個節點

此時兩個subtree各自內部節點的排列順序已經確定, 我們要的是x, y在確定順序下的排列方式
ex. x = {x1, x2, x3}; y = {y2, y1}
相當於總共有x+y個位置, 我們任選三個位置依順序放入 {x1 x2 x3}, 其餘位置依序放入{y2, y1}
y2 y1 x1 x2 x3
y2 x1 y1 x2 x3
y2 x1 x2 y1 x3
y2 x1 x2 x3 y1
...
如此下去

因此這個**"這兩種分支的排列方式"** = math.comb(x+y, y)

# What if we don't have math.comb?

[@HuifengGuan](https://www.youtube.com/watch?v=yfBHIDVN8Vs&ab_channel=HuifengGuan)的影片裡有說明此題解法以及該如何計算

雖然在思考邏輯上不大一樣, 但本質都是在求排列的數目

```
res = res * ways * (math.comb(x+y, y) % mod)

math.comb(x+y, y) % mod = (factorial(x+y) / factorial(y)) % mod
```

除法是沒有餘數相關性質的, factorial(x+y) % mod / factorial(y) 會出錯
只有乘法有餘數性質

但由於mod是質數, 在mod是質數的情況下, 兩式同餘的情況我們可以將上式表達成:

```
x / y = x * (1/y) % mod = x * inv_y % mod
```

也就是說:

```
math.comb(x+y, y) % mod = (factorial(x+y) / ((factorial(x)) * factorial(y))) % mod
                        = (factorial(x+y) * (1/factorial(y)) * (1/factorial(y))) % mod
                        = (factorial(x+y) * (inverse(factorial(x)) * inverse(factorial(y)))) % mod
```

而這個inv_y可以有些數學計算來快速計算出來

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

所以原dfs可改成:

1. 費馬小定理

```py
fac = [1] * (n+1)
fac_inv = [1] * (n+1)
for i in range(2, len(fac)):
    fac[i] = fac[i-1]*i%mod
    fac_inv[i] = pow(fac[i], mod-2, mod)

def dfs(i):
    if len(graph[i]) == 0: # leaf nodes
        return 1, 1 # (number of ways, number of nodes)
    
    res = 1
    x = 0
    for nxt in graph[i]:
        ways, y = dfs(nxt)
        comb =  (((fac[x+y] * fac_inv[x]) % mod) * fac_inv[y]) % mod
        res = (res * ways % mod) * comb % mod
        x += y

    return res, x + 1
```

2. 函式計算

```py
fac = [1] * (n+1)
for i in range(2, len(fac)):
    fac[i] = fac[i-1]*i%mod

def inv(x: int):
    s = 1
    while x > 1:
        s = s * (mod - mod//x) % mod
        x = mod%x
    return s

def dfs(i):
    if len(graph[i]) == 0: # leaf nodes
        return 1, 1 # (number of ways, number of nodes)
    
    res = 1
    x = 0
    for nxt in graph[i]:
        ways, y = dfs(nxt)
        comb =  (((fac[x+y] * inv(x)) % mod) * inv(y)) % mod
        res = (res * ways % mod) * comb % mod
        x += y

    return res, x + 1
```