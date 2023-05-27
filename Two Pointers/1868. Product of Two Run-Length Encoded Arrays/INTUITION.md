# Intuition

一開始很直覺想到的是:
我們用two pointers來指向encoded1跟encoded2
並且持續相乘

```py
res = []
while i < n and j < m:
    curr = encoded1[i][0] * encoded2[j][0]
    encoded1[i][1] -= 1
    encoded2[j][1] -= 1
    if encoded1[i][1] == 0:
        i += 1
    if encoded2[j][1] == 0:
        j += 1

    if not res or res[-1][0] != curr:
        res.append([curr, 1])
    else:
        res[-1][1] += 1
```

但很明顯的每個數值的頻次最高到10^4, 顯然一個一個相乘是沒有效率的
實際上我們做了很多多餘的操作

當我們有`encoded1[i]`跟`encoded2[j]`時
由於是長度相等兩個兩個配對相乘, 其實最終就是把頻次較小或相等的個數拿出來配對相乘並且進行run-length encoded
所以每次的操作其實我們都有這麼多個相同的相乘`k = min(encoded1[i][1], encoded[j][1])`
我們應當一次扣除掉`k`個相同操作的配對