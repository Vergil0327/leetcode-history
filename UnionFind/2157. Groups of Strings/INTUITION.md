# Intuition

words[i]可以透過三種操作跟這些可能字詞連接在一起
set(words[i]) replace words[i][j] with a-z
set(words[i]) add a-z to j-th position
set(words[i]) delete any j-th character

透過union-find能知道有多少個group以及最大group size
重點還是如何高效判斷words[i], words[j]是connect在一起的

那麼每個words[i]就相當於是個節點, 透過三種操作找出可能words[j]
然後union(words[i], words[j])
最終找出connected componenet的個數以及最大size即可

> 根據constraint: No letter occurs more than once in words[i].
由於每個字母只會出現一次, 比起直接compare(words[i], words[j])
我們可以將words[i]轉為bitmask, 用長度26的二進制編碼紀錄哪些位置

然後透過三種操作找出words[j]並透過union-find進行union
最後看有多少group及其最大size即可

首先是`replace`操作
對於當前的index=i, words[i] = bit來說

我們可以找出我們有哪些字符, 把他替換成我們沒有的字符: O(26*26)

```py
for j in range(26):
    if (bit>>j)&1: # replace existed one
        for k in range(26):
            if (bit>>k)&1: continue

            new_bit = bit
            new_bit ^= (1<<j)
            new_bit ^= (1<<k)
            if new_bit in index:
                union(i, index[new_bit])
```

由於我們也可以將當前的字母換成一樣的字母, 也就是words[i]不變
也就是關於duplicate words[i]的部分, 他們肯定也是都是connected的
所以這部分我們也要union一下, 我們可以在求index的時候順帶處理

由於我們需要在union的時候, 需要查看當前操作後的possible word存不存在
並透過index作為key進行union
因此我們得找一下每個words[i]的index是多少, 方便我們之後進行union
如果是相同的dupliate words[i], 我們也能在這步直接就先union起來

```py
index = {}
for i, bit in enumerate(arr):
    if bit in index:
        union(i, index[bit])
        index[bit] = find(i)
    else:
        index[bit] = i
```

再來是`add`跟`delete`操作:
但words[j] +1 character 後如果變成words[j]
代表words[j] -1 character 後會變成words[i]
這兩個步驟其實是一樣意思, 所以我們就擇一即可
這部很簡單, 我們挑選`delete`, 把字母刪掉, 查看存不存在並進行union即可, time:O(26)
```py
for i, bit in enumerate(arr):
    for j in range(26):
        if (bit>>j)&1:
            new_bit = bit^(1<<j)
            if new_bit in index:
                union(i, index[new_bit])
```

time complexity: O(n*26*26)


# Optimzed

關於replace這項操作

words[i] -> -1 character -> +1 character -> 得到words[j]

我們可以換個角度, 我們將words[i] `-1` character 得到 x
再將words[j]也 -1 character 得到 y

如果 x==y, 那代表words[i]能透過replacement變成words[j]
這樣我們就能將(O26*26)降為O(26)

```py
# replace
MAP = {}
for i, bit in enumerate(arr):
    for j in range(26):
        if (bit>>j)&1 == 0: continue
        # replace existed one
        x = bit^(1<<j)
        if x in MAP:
            union(i, MAP[x])
        MAP[x] = i
```