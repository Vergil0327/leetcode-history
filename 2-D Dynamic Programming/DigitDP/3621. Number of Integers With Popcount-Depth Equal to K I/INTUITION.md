# Intuition

從 example 2 來看, 重點是1-bits的數目
"11", "101", "110"都是2個1-bit, 然後三者的popcount路徑都相同
所以看來可以用dp來加總類似計算, 透過memorization來避免重複計算?

再來想到可以透過digit DP來建構範圍[1,n]的binary string, 那這樣`1 <= n <= 10^15`如果以binary string表示
binary string length也才[1, log2(10^15) ~ 50]

那既然最多只會有約50個1-bit, 我們可以預先計算出這範圍內的depth[popcount(num)]: steps of popcount of num

```py
depth = [0] * 51
for i in range(2, 51):
    depth[i] = depth[i.bit_count()]+1
```

如果 popcount-depth 是`k`, 那麼就是`k-1` steps
那再來就是用digit dp去建構出[1,n]範圍內的所有可能binary string, 找出有多少個`depth == k-1`的合法數了