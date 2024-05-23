# Intuition

首先n本身就是個符合consecutive positive integers的寫法
所以ex.2 n = 9 = 4+5 = 2+3+4 共3種寫法

```
n = k + (n-k)          => 如果是連續數:  n-k = k+1 => n = k + k+1
  = k + k+1 + (n-2k-1) => 如果是連續數:  n-2k-1 = (k+1)+1 => n = k + k+1 + k+2
  = k + k+1 + k+2 + (n-k-(k+1)-(k+2)): n-k-(k+1)-(k+2) = k+3 => n = k + k+1 + k+2 + k+3
```

1. 遍歷k求連續m個數的話: n = (k+(k+m-1)) * m / 2
=> (2k+m-1)*m = n*2 
=> m^2 + (2k-1)m - 2n = 0 => m = (-(2*k-1) + sqrt(pow(2, 2*k-1) - 4*(-2*n))) / 2
=> 會有個sqrt

2. 遍歷m求k的話: n = (k+k+m-1) * m / 2
=> 2*n / m = 2*k + m - 1
=> k = ((2*n/m) - m + 1)/2
=> 沒有sqrt, 只是單純加減乘除 => 明顯比較簡單

所以我們就能有個brute force去遍歷m求k, 連續m個數加起來要等於n, 連續數`m`的上限大概抓個 n/2 (舉幾個例子會發現不可能超過這數目)
並且連續m個數的話, 還必須滿足 **k > 0 並且 k+m-1必須 <= n**
所以可得到:

```py
res = 0
for m in range(1, ceil(n/2)+1):
    k = ((2*n/m) - m + 1)/2
    if k.is_integer() and k+m-1 <= n and k > 0:
        res += 1
    elif k <= 0 or k+m-1 > n:
        break

return res
```

然後這brute force就意外通過了

如果回到上面遍歷k求m這式子的話: m = (-(2*k-1) + sqrt(pow(2, 2*k-1) - 4*(-2*n))) / 2
m上限大概能取個 sqrt(8*n), 所以也能比較有根據地寫成

```py
res = 0
for m in range(1, ceil(sqrt(8*n))+1):
    k = ((2*n/m) - m + 1)/2
    if k.is_integer() and k+m-1 <= n and k > 0:
        res += 1
    elif k <= 0 or k+m-1 > n:
        break

return res
```

# Other Approach

另有log(n)的數學解, 但太過複雜就算了

```py
def consecutiveNumbersSum(self, N):
    res = 1
    i = 3
    while N % 2 == 0:
        N /= 2
    while i * i <= N:
        count = 0
        while N % i == 0:
            N /= i
            count += 1
        res *= count + 1
        i += 2
    return res if N == 1 else res * 2
```