# Intuition

這題是個觀察題, 重點就是Hint 1, 沒觀察到就無從下手
仔細看會發現, 其實每個character的cost只跟他出現的次數有關
因為當前字母的cost只跟他先前出現多少次有關, 

如果字母`x`出現1次, 那`x`造成的cost = 0
如果字母`x`出現2次, 那`x`造成的cost = 0 + 1
如果字母`x`出現3次, 那`x`造成的cost = 0 + 1 + 2
...

那既然跟順序無關, cost只跟frequency有關

那對於每個"?", 我們就greedily assign當前frequency最小的字母

```py
count = Counter(s)

pq = [] # [cost, character]
for c in string.ascii_lowercase:
    heapq.heappush(pq, (count[c], c))

replacement = []
for c in s:
    if c == "?":
        count, ch = heapq.heappop(pq)
        replacement.append(ch)
        heapq.heappush(pq, (count + 1, ch))
```

那這樣我們就知道我們要把"?"改成哪些字符, 由於我們要lexicographically smallest
所以我們替代字符依照字典順序排序(或是直接用min heap), 然後再依序替換掉"?"即可

```py
replacement.sort(reverse=True)
res = ""
for c in s:
    if c == "?":
        res += replacement.pop()
    else:
        res += c
return res
```

