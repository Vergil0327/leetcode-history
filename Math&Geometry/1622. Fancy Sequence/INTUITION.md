# Intuition

最直觀的brute force:

```py
class Fancy:
    def __init__(self):
        self.seq = []
        self.mod = 10**9 + 7
    def append(self, val: int) -> None:
        self.seq.append(val)
    def addAll(self, inc: int) -> None:
        mod = self.mod
        self.seq = [(num+inc)%mod for num in self.seq]
    def multAll(self, m: int) -> None:
        mod = self.mod
        self.seq = [(num*m)%mod for num in self.seq]
    def getIndex(self, idx: int) -> int:
        if idx < 0 or idx >= len(self.seq): return -1
        return self.seq[idx]
```

idx最高有10^5, 這樣再計算那就會是O(n^2)超時
所以再來想到的是, 我們需要的時候再計算, 先把每個值的操作都先記住然後再getIndex再計算
這樣除了getIndex會是O(n)外, 其他都是O(1)

```py
class Fancy:

    def __init__(self):
        self.seq = []
        self.op = []
        self.opIdx = [-1]
        self.start = 0
        self.mod = 10**9 + 7

    def append(self, val: int) -> None:
        self.seq.append(val)
        self.opIdx.append(-1)
        self.opIdx[len(self.seq)-1] = self.start

    def addAll(self, inc: int) -> None:
        if not self.op or self.op[-1][0] == "*":
            self.op.append(["+", inc])
        else:
            self.op[-1][1] = (self.op[-1][1] + inc)%self.mod
        
        self.start += 1

    def multAll(self, m: int) -> None:
        if not self.op or self.op[-1][0] == "+":
            self.op.append(["*", m])
        else:
            self.op[-1][1] = (self.op[-1][1] * m)%self.mod
        
        self.start += 1

    def getIndex(self, idx: int) -> int:
        if idx < 0 or idx >= len(self.seq): return -1

        for i in range(self.opIdx[idx], len(self.op)):
            operator, val = self.op[i]
            if operator == "+":
                self.seq[idx] += val
            elif operator == "*":
                self.seq[idx] *= val
            self.seq[idx] %= self.mod
        self.opIdx[idx] = len(self.op)
        return self.seq[idx]
```

結果還是在105/107 test cases超時, 當下思緒就卡死了

> 參考[@HuifengGuan 影片詳細說明](https://www.youtube.com/watch?v=JnEi4QPKhhk&ab_channel=HuifengGuan)

但其實這邊還有個想法是, 如果先不管modulo, 能不能都以O(1)時間計算出來?

我們儲存了每個數值的operator

op = [["*", m1], ["+", inc1], ...]

seq[0] = seq[0] apply op[opIdx0:] = (seq[0] apply inverse op[:opIdx0-1]) apply op[0:n-1]

其實有點像prefix sum的概念

我們希望seq[0] apply 這段operations `op[opIdx0:]`
而這可以等同於我們持續更新accumate operation `op[0:n-1]`, 然後我們seq[0]存的是inverse op[:opIdx0-1], 其中inverse op[:opIdx0-1]指的是如果原本要乘上`m` 那麼`seq[0]=seq[0]/m`

那這樣seq[0]再加上整段`op[0:n-1]`操作, 就會是想要的答案

示意圖如下:

```
seq = [a   b   c   d]
         +   *   +
         x   y   z
```

seq[0] = ((a+x) * y) + z
seq[1] = (b*y) + z = (((b-x) +x) * y) + z
seq[2] = c+z = ((c/y) * y) + z = (((c/y - x) + x) * y) + z
seq[3] = d

那如果全部操作化簡成* MUL + INC的話:
seq[0] = num0 * MUL + INC
seq[1] = (num1/b) * MUL + INC
       = ((num1-INC') / MUL') * MUL + INC 其中 * MUL' + INC'就是截至num1為止的所有操作

因此在先不考慮modulo的情況下則為:

```py
class Fancy:
    def __init__(self):
        self.mul, self.inc, self.mod = 1, 0, 1000000007
        self.num = []

    def append(self, val: int) -> None:
        self.num.append([val, self.mul, self.inc])

    def addAll(self, inc: int) -> None:
        self.inc += inc

    def multAll(self, m: int) -> None:
        self.mul = self.mul * m
        self.inc = self.inc * m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.num): return -1
        
        v, v_mul, v_inc = self.num[idx]

        inverse_v = (v-v_inc) / v_mul
        return (inverse_v * self.mul + self.inc) % self.mod
```

再來這邊就需要數學知識了, 由於我們最終結果需要對mod取餘
但除法是不像乘法那樣有同餘定理性質的

inverse_v = ((v-v_inc) / v_mul) % mod ≠ (v-v_inc)%mod / v_mul %mod
          = (v-v_inc)%mod * inv(v_mul)%mod

而這個inverse element `inv(v_mul)`, 在v_mul跟mod互質的情況下:

```py
inv(v_mul) = pow(v_mul, mod-2, mod) # 費馬小定理
```

所以原本的:

```
(inverse_v * self.mul + self.inc) % mod
=> (((v-v_inc) / v_mul) * self.mul + self.inc) % mod
=> (v * self.mul/v_mul - v_inc * self.mul/v_mul + self.inc) % mod
=> v * (self.mul * inv(v_mul) % mod) - v_inc * (self.mul * inv(v_mul) % mod) + self.inc%mod
=> (v * x - v_inc * x + self.inc)%mod where x = self.mul * inv(v_mul) % mod
```