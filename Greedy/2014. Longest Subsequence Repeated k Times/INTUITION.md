# Intuition

要找出重複`k`次的subseq, 代表:
1. 必須是至少出現k次的letter
2. subseq長度不超過len(s)/k

所以我們可以先從s當中找出符合的letter, 並且看有多少個能用

```py
count = Counter(s)
validLetters = [ch for ch, freq in count.items() if freq >= k]
```

而每個validLetters要組成subseq的話, 他們每個letter共有freq//k個可選
所以我們先找出, 每個letter都選的subseq:

```py
subseq = "".join(ch*(freq//k) for ch, freq in count.items() if freq >= k)
```

那再來我們在搜索出所有可能的subseq:
1. 找出每個長度的所有可能subseq, 也就是該長度的letter combination, 
2. 再找出每個subseq的permutation
如此一來即可得到所有可能subseq

```py
subseq = "".join(ch*(freq//k) for ch, freq in count.items() if freq >= k)
possible = set()
for size in range(len(subseq)+1):
    for candidate in combinations(subseq, size):
        for ss in permutations(candidate):
            possible.add("".join(ss))
```

所們把所有subseq夾到hashset裡後, 接下來該subseq能不能在s裡面找出至少k個來, 返回符合條件的即可
找的方式也很簡單, 我們用greedy的方式去看能組出多少該subseq即可

```py
def greedy_find(t):
    if not t: return 0
    cnt = j = 0
    for ch in s:
        if ch == t[j]:
            j += 1
        if j == len(t):
            cnt += 1
            j = 0
    return cnt

res = ""
for ss in possible:
    cnt = greedy_find(ss)
    if cnt >= k:
        res = max(res, ss, key=lambda x:(len(x), x))
return res
```

但這樣會TLE, 轉念想
我們可以改對所有可能subseq先排序, 以長度跟字典序做排序, 這樣的話我們改成返回第一個合法的subseq即可

```py
def greedy_find(t):
    if not t: return 0
    cnt = j = 0
    for ch in s:
        if ch == t[j]:
            j += 1
        if j == len(t):
            cnt += 1
            j = 0
    return cnt

for ss in sorted(possible, key=lambda x:(len(x), x), reverse=True):
    cnt = greedy_find(ss)
    if cnt >= k:
        return ss
return ""
```

# Analysis

但這本質上是對所有subseq進行暴力搜索, 然後再做排序
最後再以O(subseq.size * s.length)搜索出合法解
為什麼時間上允許?

因為底下有個限制: `2 <= n < k * 8`, 這行代表其實我們的subseq最多只會有7個字母

因為我們有至少k個subseq, 必須滿足`subseq.length * k <= n`
但`n < k*8`

所以為了同時滿足兩個不等式 => `subseq.length * k <= n < k*8`
=> `subseq.length < 8`

所以我們暴力搜索subseq所花的時間複雜度僅需要: O(2^7 + 2^7log(2^7) + 2^7 * n) = O(2^7 * n)