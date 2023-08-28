# Intuition

2,2,2,5,5

為了滿足**nice**, 每個prime factor必須至少有1個
=> {2,5}必選

然後留下{2,2,5}

{2,2}, {5}, 依據各個prime factor
=> {2都不選, 選1個, 選兩個} * {不選5, 選1個5}
=> {_, 2, 22} * {_, 5}
=> 3個選擇 * 2個選擇 = 6

所以example.1{2,2,2,5,5}這些prime factor, 才共有6個nice divisors

知道如何計算number of nice divisors後, 再來就是看如何找出能組出最多nice divisors的prime factor組合

看起來我們並不關心選了哪些prime factor, 我們只關心他們的組合
如果我們最多有`primeFactors`個: primeFactors = A + B + C + D + ...

要使得nice divisors最多, 代表`primeFactors`要盡可能平均的拆分, 這樣乘積才會最大
```
ex. primeFactors = A + B + C + ...
ex. primeFactors = 6 = 1 + 5 => 1*5個nice divisors
                     = 2 + 3 => 2*3個nice divisors
```

所以如果`primeFactors=n`拆成k份, 那共有`k`份`n/k`, 我們要讓這個乘積最大所以是: `maximize{ (n/k)^k }`
數學解來說要maximize`f(k) = (n/k)^k` => 求f'(n/k) = 0 => n/k = e = 2.71...
所以盡可能將primeFactors拆成`3*3*3*3...`如果不能拆成3的話就拆成2
所以會是`primeFactors = 3*3*3*3*3*... * 2*2*2*2...`

實際上也可以這樣想: 4 = 2*2, 5的話可以拆成2*3, 6的話拆成3*3, 如果是2*2*2換成3*3更好
所以就盡可能拆成3然後不行在拆成2

edge case:
primeFactors = 1 => 1個nice
primeFactors = 2 => 分成1種 => 2個nice
primeFactors = 3 => 分成1種3個 => 3個nice