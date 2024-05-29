
# Intuition

TOP: O X X O O X O X

首先想到是從第一排出發, 將相鄰元素利用union-find組在一起
再來就遍歷`[i, j] = hits`:
1. 如果grid[i][j] == 0: 不影響掉落, append(0)
2. 如果grid[i][j] == 1: 我們就拿掉磚塊, 如果我們陸續拿掉磚塊的話會發生下面這樣的變化

```
 [1,0,0,0],
 [1,1,1,1],
 [1,0,1,0]
-> remove (1,1)
 [1,0,0,0],
 [1,0,1,1],
 [1,0,1,0]
-> remove (1,0)
 [1,0,0,0],
 [0,0,1,1],
 [1,0,1,0]
```

最後看到所有沒跟第一排相連的connected component, 都是會掉落的bricks
當順著拿掉hits的時候, 我們要考慮拿掉後的四個方向的connected component還尚存多少個stable brick, 只要還與第一排有相連, 那就不會掉落
如果是brute force的話, 變成我們每次都要check整個connected component一次來計算他還剩多少brick與天花板相連

但如果我們從最後的狀態反過來的話, 每當我們加回去一個磚塊
會發現我們一樣可以只check四個方向的connected componenent, 一但有任一connected componenet原本是沒跟solid connected componenet連接再一起的話
代表我們加回來的這塊磚塊是當下他的最後一個支撐點, 所以回到我們拿掉這塊磚塊的時候, 這個connected component是會掉落的
所以當我們反過來逐步加回磚塊時, 我們可以將所有原本沒跟天花板相連的connected componenet數量全加總起來, 計作**x**, 這個**x**就是掉落的磚塊數
計算完後再將這些connected componenet union再一起形成solid connected component
這樣從最後一個狀態逐步推回來後, 就能計算出每個當下的掉落磚塊數了

為了方便我們查知當前的connected componenet有沒有跟天花板相連, 我們將(row, col)轉成`id = row*col+col`
然後在union的時候一率將parent union到最靠上方的那塊, 這樣我們就能再透過id轉回(row, col)並查看是不是與天花板相連

## Union-Find
```py
toId = lambda r, c: r*n+c
parent = list(range(m*n))
rank = [1]*(m*n)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px == py: return

    rowx, rowy = px//n, py//n
    if rowx < rowy:
        rank[px] += rank[py]
        parent[py] = px
    else:
        rank[py] += rank[px]
        parent[px] = py
```

然後移除掉hits: 注意題目有說hits有可能原位置是空

```py
# remove hits
for i, j in hits:
    if grid[i][j] == 0: continue
    grid[i][j] = -1 # mark removed bricks
```

最後在逆著把hits的磚塊放回來並逐步union即可
但要注意的是, 放回磚塊的四個方向並不一定都是分別獨立的connected componenet
所以還外用個hashset來紀錄是否計算過
不然有可能會變成右邊會墜落, 但其實跟下方是連通的, 等到我們計算下方的時候會重複計算

等到四個方向查證完後, 最後在看這四個方向有沒有因為當下放回去這塊brick而跟天花板相連
如果有相連, 那麼這瞬間才會因為這磚塊而墜落

```py
res = []
for r, c in reversed(hits):
    if grid[r][c] == 0:
        res.append(0)
        continue
    
    grid[r][c] = 1
    cnt = 0
    counted = set()
    for dr, dc in dirs:
        row, col = r+dr, c+dc
        if row<0 or row>=m or col<0 or col>=n: continue
        if grid[row][col] == 0 or grid[row][col] == -1: continue

        p = find(toId(row, col))
        pRow = p//n
        if pRow != 0 and p not in counted: # not solid
            counted.add(p)
            cnt += rank[p]

        union(toId(r, c), p)

    # 檢查是否因為當前(r,c)這塊磚塊而墜落
    # => 就檢查當前的這些falling bricks是否因為(r,c)這磚塊而連接回天花板
    p = find(toId(r, c))
    if p//n == 0:
        res.append(cnt)
    else:
        res.append(0)
return reversed(res)
```

但其實也不需要hashset `counted`, 根據[@HuifengGuan](https://www.youtube.com/watch?v=mPT6ow3MbXw&ab_channel=HuifengGuan)的影片解說, 我們可以改成這麼判斷

在四個方向跟磚塊union時, 對於那些還沒跟當前磚塊union的
- 假如他沒跟天花板連接, 那麼紀錄到cnt裡
- 如果磚塊本身就在天花板, 或是其他connected componenet有連接到天花板的話, 我們標示`connectTop=True`
- 最後只有`connectTop=True`這情況下, 當前的這些`cnt`才會墜落

```py
for r, c in reversed(hits):
    if grid[r][c] == 0:
        res.append(0)
        continue
    
    grid[r][c] = 1
    cnt = 0
    connectTop = False
    for dr, dc in dirs:
        row, col = r+dr, c+dc
        if row<0 or row>=m or col<0 or col>=n: continue
        if grid[row][col] == 0 or grid[row][col] == -1: continue
        
        p1, p2 = find(toId(row, col)), find(toId(r, c))
        if p1 == p2: continue

        pRow = p1//n
        if pRow == 0 or r == 0:
            connectTop = True

        if pRow != 0: # not solid
            cnt += rank[p1]
        union(p1, p2)

    res.append(cnt if connectTop else 0)

```