# Intuition

看完題意的想法是
選好一個方向的目的地就一直走, 直到到定位或是兩個棋子在同一格及越界
n很小, 感覺能暴力搜索出全部combination

首先想到
棋盤就8*8格, 棋子最多4個
8*8 = 64 => 能用2^64 每個棋子都能用bitmask標示出位置 ex. 10000000
如果相互AND不為0 => invalid, 有複數棋子在同一格位置

所以能先將positions轉為bitmasks形式

```py
m = n = 8
bitmasks = [1<<(r*n+c)for r, c in positions]
```

再來決定每個棋子的方向進行組合:

首先每個棋子的所有可能方向組合在一起為

```py
destinations = []
for p in pieces:
    if p == "rook":
        destinations.append(list(range(len(dirs1))))
        
    elif p == "queen":
        destinations.append(list(range(len(dirs))))

    else: # bishop
        destinations.append(list(range(len(dirs2))))
dir_combinations = product(*destinations)
```

既然有了方向, 再來就是用個變量`stop`決定每個棋子走到目的地了沒
一樣能用bitmask, ex. 1011表示(1st, 2nd, 4-th)都還在前進而3rd已到達目的地停了下來(用0在bitmask上表示)

那這樣看來, 我們僅需要用方向組合跟`stop`變量就能知道每個棋子該怎麼移動
我們就能用dfs去搜索出全部可能了

4個棋子最多走8格, 8^4種可能組合(每個棋子有8格目的地可選)
那方向組合最多就: 8*4*4*4 (最多1個皇后, 剩下的rock, bishop都只有四種方向)
所以time upperbound: 8^4 * (8*4*4*4) ~ 2 * 10^6 => 可接受的時間範圍 (leetcode時限約為10^6級別)
這分析更證明這題能用dfs去暴力搜索全部可能

整個框架就是:

```py
pos = [1<<(r*n+c)for r, c in positions]
for dir_mask in product(*destinations):
    i = len(pieces)
    stop = (1<<i)-1
    dfs(pos, dir_mask, stop)
```

那每層遞歸的時候, 都要考慮正在行進的棋子要不要停下來, 而停下來的就不能再走了
所以對於當前的`stop` mask, 假設是110, 那麼他下一步只可能是`110`, `100`, `010`, `000`, 不可能出現`001`這類的停止又在行進的mask
所以對於遍歷stop的next state, 我們可以透過stop&nxt_stop == next_stop來判斷next_stop合不合法
然後就能持續更新pos並搜索
但反正是暴力搜索, encode pos好像有點多此一舉, 所以我們直接帶入positions就好

```py
for dir_mask in product(*destinations):
    i = len(pieces)
    stop = (1<<i)-1
    dfs(positions, dir_mask, stop)
```

那再來我們就用dfs去搜索全部可能, 並把valid position放入hashset, 最終hashset.size即為答案
其中用`check`這個helper func去檢查有沒有位置是越界或是棋子落在同一格的

```py
def check(pos):
    occupied = set()
    for r, c in pos:
        occupied.add((r,c))
        if r <= 0 or r > 8 or c <= 0 or c > 8:
            return False
    if len(occupied) < len(pos): return False

    return True

self.res = set()
def dfs(pos, dirmask, stop):
    if stop == 0: return # all stopped

    self.res.add(tuple(pos))

    for nxt_stop in range(1<<len(dirmask)):
        if stop & nxt_stop != nxt_stop: continue

        new_pos = pos.copy()
        for i in range(len(new_pos)):
            did_stop = (nxt_stop>>i)&1
            new_pos[i] = (new_pos[i][0] + dirmask[i][0]*did_stop, new_pos[i][1] + dirmask[i][1]*did_stop)

        if not check(new_pos): continue
        dfs(new_pos, dirmask, nxt_stop)
```