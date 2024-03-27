# Intuition


題意:

1. Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
2. Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for all the possible values of k in the range [i, j] inclusive.
3. Swap the two characters at indices i - 1​​​​ 
4. Reverse the suffix starting at index i​​​​​​

ex. s="cba"

cb{a} -> cab -> reverse -> cab
c{ab} -> bac -> reverse -> bca
bc{a} -> bac -> reverse -> bac
b{a}c -> abc -> reverse -> acb
ac{b} -> abc -> reverse -> abc


首先看出s[i:j]會是sorted string with duplicates, 且都小於s[i-1]
但並沒有多大幫助

這題最關鍵的觀察是:

cba -> cab: 經過操作後我們所得到的是什麼? => 得到的其實是previous smaller permutation
cba -> cab -> bca -> bac -> acb -> abc
箭頭反向後就會是leetcode 31. next permutation

這樣一看, 那麼其實這題問的就是有多少個比s還小的permutation (或是問這個s, 依據lexicographic是第幾個permutation)

得出這結論後, 我們朝permutations去想

ex. s = C {F X X X X X X X X}

後面suffix裡, 如果有x個字母小於C, 那就代表這X個可以放到首位, 那們剩下字母的所有排列都會使得permutation小於s
假設後面suffix有k個, 那就是`x * k!`種排列
但別忘記要扣掉重複排列, 所以首位小於C時permutaiton為: `x * k! / (duplicate1! * duplicate2! * ...)`

然後再來就看下一位: ex. C F {X X X X X X X X}, 並重複一樣步驟 (此時首位以確定是C, 這時的duplicate的字母僅需考慮s[i+1:])
從後面字母找到比F小的都可以替換, 然後一樣有 k' / (factorial(# of duplicate 1) * factorial(# of duplicate 2) * ...)

因此我們會得到

```py
n = len(s)
mod = 10**9 + 7

count = Counter(s)

res = 0
for i in range(n):
    numSmaller = 0
    for ch in string.ascii_lowercase:
        if ch >= s[i]: break
        numSmaller += count[ch]

    numPermutations = numSmaller * factorial(n-i-1)
    # remove duplicate permutations
    for freq in count.values():
        numPermutations //= factorial(freq)

    res = (res + numPermutations) % mod
    count[s[i]] -= 1
    if count[s[i]] == 0:
        del count[s[i]]
return res
```

可惜這樣會TLE, 這邊有幾個能優化的點是:

1. factorial(n-i-1)我們能提前處理並取modulo

```py
fac = [1]*(n+1)
for i in range(2, n+1):
    fac[i] = fac[i-1]*i%mod
```

2. 除法沒有相關特性, 不能提早取modulo, 必須求出他的inverse使得 (a / b) % mod = a * inv(b) % mod

```py
def inv(x):
    s = 1
    while x > 1:
        s = s * (mod - mod//x) % mod
        x = mod%x
    return s

numPermutations = numSmaller * fac[n-i-1]
# remove duplicate permutations
for freq in count.values():
    numPermutations = numPermutations * inv(fac[freq]) % mod
```

# Other Approach

從後往前一個個來對我來說比較不直覺, 但原文章詳解[在這](https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/solutions/1163050/python-o-26n-math-solution-explained/)

```py
class Solution:
    def makeStringSorted(self, s: str) -> int:
        counter, prod, res, mod = [0]*26, 1, 0, 1000000007
        for i, c in enumerate(s[::-1], 1):
            idx = ord(c)-ord("a")
            counter[idx] += 1
            res = (res + prod * sum(counter[:idx])//counter[idx]) % mod
            prod = prod*i//counter[idx]
        return res
```
