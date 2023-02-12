# Intuition

對於每個queries[i]: `[first, second] = queries[i]`

我們要找一個bit value XOR first = Second
根據XOR的特性

```
   val ^ first == second
-> val ^ first ^ first == second ^ first
-> val == second ^ first
```

所以brute force方式就是遍歷每個queries，找出第一個substring的值等於`second^first`

# Optimized

但由於bit最多就32位，所以我們可以預處理當前`s`，找出所有可能的substring的最左index
另外要注意的是由於要找的是最短substring，代表`1011`優於`01011`或是`001011`
所以我們要撇除leading zeros

```py
n = len(s)
preprocess = {}
for i in range(n):
    # we don't want leading zeros in bits
    # but we still need to store position for bit `0`
    bit = 0
    if s[i] == "0":
        if bit not in preprocess:
            preprocess[bit] = [i, i]
        continue

    for j in range(i, min(i+32, n)):
        bit = (bit<<1) | int(s[j])
        if bit not in preprocess:
            preprocess[bit] = [i, j]
```

但要特別注意`0`這個case，我們也要記錄當`second^first`為`0`時最左index
```py
bit = 0
if s[i] == "0":
    if bit not in preprocess:
        preprocess[bit] = [i, i]
    continue
```