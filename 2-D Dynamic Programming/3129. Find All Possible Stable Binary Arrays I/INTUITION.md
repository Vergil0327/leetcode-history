# Intuition

limit個 00...0 or 11...1

{X X X X X X X} 0
必須確保前面limit個必須至少有個1

{X X X X X X X} 1
必須確保前面limit個必須至少有個0

brute force: 紀錄前次limit個"1", "0"分佈 (Memory Limit Exceeded)

```py
@cache
def dfs(zero, one, subarr):
    if zero == 0 and one == 0: return 1

    res = 0
    if len(subarr) < limit:
        if zero > 0:
            res += dfs(zero-1, one, subarr+"0")
        if one > 0:
            res += dfs(zero, one-1, subarr+"1")
    else:
        count = Counter(subarr)
        
        
        if zero > 0 and count["1"] > 0:
            res += dfs(zero-1, one, subarr[1:]+"0")
            
        if one > 0 and count["0"] > 0:
            res += dfs(zero, one-1, subarr[1:]+"1")
    
    return res
```

但既然是往dp去想, 比起關注前limit個"1"或"0"我們是怎麼選擇的
我們就關心第i-1次我們是放置"0"還是"1"就好

如果第i-1次最後放的是1, 那代表我們後面limit個位置都可以放置0, 我們可以選擇放置:
1. 連續1個0
```
i-1   i
1     0
```

2. 連續2個0
```
i-1   i
1     00
```

3. 一直到連續limit個0都是可以的
```
i-1   i
1     0...0
```

然後下次我們就考慮放置多少個連續個"1"

這樣交替放置數個連續0跟連續1後, 利用dfs搜索, 最終就能知道有多少個合法解