# Math

## Intuition

permutation without duplicates:

```
permutations = n! / (# of each character)!
```

ex. "hot", permutations = `3!` = `3x2x1`

ex. "too", permutations = `3!/2!`

total distinct permutations = multiply all the permutations

## Approach

這題直接套用python built-in `math.factorial` 可以過
但如果要自己算的話會超時，這是因為我們要除各個重複數的factorial時，數值可能很大
但除法又不能取餘，因此這時我們可能要用到一個數學技巧，取modular inverse

將以下這段除法
```python
perms = factorial(len(word))
for freq in counter.values():
    perms //= factorial(freq)
```

改為乘法取餘
```python
res *= fact[len(word)]
for freq in Counter(word).values():
    res *= invFact[freq]
```

參考這篇[solution](https://leetcode.com/problems/count-anagrams/solutions/2946557/c-java-python3-multinomial-coefficients/)及這篇[Modular Inverse](https://cp-algorithms.com/algebra/module-inverse.html#finding-the-modular-inverse-using-binary-exponentiation)可知

由於我們的MOD, `1e9+7`, 是質數，因此

$a^(m-1)$ = 1 % MOD
同 * a^-1後變為
$a^(m-2)$ = $a^(-1)$ % MOD

因此我們的inverse factorial即可轉為`pow(num, MOD-2, MOD)`的形式來事先計算出來，並且原本的除法也可轉為全部都乘法取餘的模式

```python
fact = [1] * (n+1)
invFact = [1] * (n+1)
for num in range(1, n+1):
    fact[num] = fact[num-1] * num % MOD
    invFact[num] = invFact[num-1] * pow(num, MOD-2, MOD) % MOD

res *= fact[len(word)]
for freq in Counter(word).values():
    res *= invFact[freq]
```

另外如果要自己實作`pow(num, MOD-2, MOD)`的話，則為
```python
def powmod(a, b, mod): # time: O(log(b))
    if b == 0: return 1
    res = powmod(a, b//2, mod)
    if b%2 == 0: # b is even
        return res*res%mod
    else: # b is odd
        return res*res*a%mod
```

或者另外還有個更general的計算modular inverse的公式
```python
inv[1] = 1
for i in range(2, m):
    inv[i] = m - (m//i) * inv[m%i] % m
```
因此上面那段程式碼可再改成

```python
mod = 1_000_000_007
inv = [1]*(n+1)
fact = [1]*(n+1)
ifact = [1]*(n+1)
for x in range(1, n+1): 
    if x >= 2: inv[x] = mod - mod//x * inv[mod % x] % mod 
    fact[x] = fact[x-1] * x % mod 
    ifact[x] = ifact[x-1] * inv[x] % mod 
```

最後計算則為
```python
res *= fact[len(word)]
for x in Counter(word).values():
    res *= ifact[x]
```