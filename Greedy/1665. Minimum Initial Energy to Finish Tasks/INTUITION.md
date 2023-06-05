# Intuition

一開始比較直覺想到的是:

如果我們一開始有 `x` energy, 我們肯定優先先挑門檻大的作, 也就是:
`tasks.sort(key=lambda x:-x[1])`

所以我們在反過來逆推我們所需能量時, 我們先試著這麼排序:
`tasks.sort(key=lambda x:x[1])`

定義:`effort, require = tasks[i][0], tasks[i][1]`

我們每次會消耗`effort`, 但能不能做的關鍵是`require`
所以我們都需要`res = max(res+eff, req)`

```py
tasks.sort(key=lambda x:x[1])

res = 0
for eff, req in tasks:
    res = max(res+eff, req)
return res
```

但馬上會發現在Example 2 failed

觀察一下會發現example2的最佳排序為: `[[8,9],[10,11],[10,12],[2,4],[1,3]]`
以這個排序進行下面的想法就會是最佳解:
```py
res = 0
for eff, req in tasks:
    res = max(res+eff, req)
return res
```

這時觀察一下會發現這是靠差值來排序: `tasks.sort(key=lambda x:(x[1]-x[0]))`
差值的意義是每次做完tasks[i]所剩下的energy

所以反過來想, 我們實際上在執行tasks[i]時一開始剩下的energy肯定越多越好
也就是這麼排序來做:`tasks.sort(key=lambda x:-(x[1]-x[0]))`
因此逆推最低所需能量時, 就反過來排序: `tasks.sort(key=lambda x:(x[1]-x[0]))`

那實際上證明方式可以參照[by HuifengGuan](https://www.youtube.com/watch?v=PCwixttbTBc)的說明

我們就看兩個task, 並且以正解做排序(`tasks.sort(key=lambda x:(x[1]-x[0]))`)

`Task1 = (a1, m1), Task2 = (a2, m2)`
依照正解排序後, 已知結果為: `m2-a2 > m1-a1` - **eq.1**

然後我們來看先做`Task1 -> Task2`跟先做`Task2 -> Task1`會有什麼差別:

我們逆推我們所需的最低能量：
Task1 -> Task2: `res1 = max(max(a1, m1)+a2, m2) = max(max(a1+a2, m1+a2), m2)`
Task2 -> Task1: `res2 = max(max(a2, m2)+a1, m1) = max(max(a2+a1, m2+a1), m1)`

```
let
    x1 = max(a1+a2, m1+a2)
    x2 = max(a1+a2, m2+a1)
then
    res1 = max(x1, m2)
    res2 = max(x2, m1)
```

由於eq.1告訴我們 `m2-a2 > m1-a1 => m2+a1 > m1+a2`
所以可知`x2 > x1` - **eq.2**

再來, 由於`x2  >= m2+a1`並且`a1 > 0`
所以可知: `x2 > m2` - **eq.3**

綜述以上我們來看:
`Task1 = (a1, m1) -> Task2 = (a2, m2)`
- 如果`m2 < m1`
  - 由於**eq.2**告訴我們`x1 < x2`, 所以res1肯定小於res2.
  - max(x1, m2) < max(x2, m1)
- 如果`m2 > m1`
  - 由於**eq.1**跟**eq.2**可知`x2 > m2 > m1`且`x2 > x1`.
  - 那麼`res2 = max(x2, m1) > max(x1, m2) = res1`

所以不管是`m2 < m1`或是`m2 > m1`, 都會是`res1 < res2`
所以透過正解的方式排序都能保證我們求出的所需能量都會是最低的

