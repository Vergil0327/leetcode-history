# Intuition 1

每次放下方塊, 在進行區間查詢當前最高的高度 => 首先區間查詢想到segment tree
再來就看該怎麼隨著方塊落下來維護segment tree

由於方塊落下時擦邊並不算疊在上面, 所以我們利用左閉右開的形式來代表每個range
這題最核心的處理兩方塊碰撞方式就是利用左閉右開的特性, 將右端點`r`歸屬到[l, r-1] (both inclusive)這區間
更簡單的方式來想就是:當落下方塊左端點剛好切齊x軸上方塊右端點時, 是不會疊加上去的, 也就是對於方塊的右端點並不影響
所以我們疊加也是左閉右開形式, 只有當落下方塊左端點疊加在x軸上方塊的**右端點-1**位置時, 高度才會疊加
所以我們才維護一個左閉右開的區間

對於一個方塊他的左右端點落在[l, r]
我們利用segment_tree查詢[l, r) 的最高位置為`h`, 那我們就更新[l, r) (right exclusive)為`h + square_length`
排除掉`r`是為了handle方塊剛好肩並肩的狀況

例如在落下一個方塊, 他的左右端點為[r, rr], 這時他的左端點會剛好跟上個方塊的右端點靠在一起而並不重疊
而我們左閉右開的形式，就會解決這個問題, 實際上就像是r這點的距離被r-1 cover掉
所以在查詢時segment_tree.query(l, r-1)

```py
n = max(i+length for i, length in positions)
arr = [0] * (n+1)
seg = SegmentTree(arr)

res = []
for i, length in positions:
    l, r = i, i+length
    h = seg.query(l, r-1)
    for j in range(l, r):
        seg[j] = h + length
    res.append(seg.query(0, n))
return res
```

但這樣會MLE, lefti <= 10^8 and sideLengthi <= 10^6

所以我們換個方式想, 由於positions <= 1000
就算每次方塊落下都有疊加, 一個interval也頂多變成兩個來維護
總共也就2000個, 所以我們可以直接用O(n^2)方式來維護並持續更新下落後的各個不同高度的interval
並持續更新全局最高的height放入`res`裡
框架如下:

```py
intervals = SortedList() # [r, l, height]
maxH = 0
res = []
for l, length in positions:
    r = l+length
    
    endIdx = intervals.bisect_right([r, -inf, -inf]) # upperbound: 第一個大於`r`位置的interval

    # find max height `h` within [l, r]
    h = 0
    for i in range(endIdx):
        left, right, height = intervals[i]
        if right < l: continue
        h = max(h, height)
    h += length

    intervals.add([l, r-1, h])
    maxH = max(maxH, h)
    res.append(maxH)
return res
```

# Intuition 2

但其實segment tree還是最直觀的
其實也是能做的, 只是必須得先對資料離散化

[great explanation by @HuifengGuan](https://www.youtube.com/watch?v=d7kSgkC32uY&ab_channel=HuifengGuan)

我們只關注每個方塊的左右端點, positions.length <= 1000, 那這樣頂多就2000個節點
相比我們一開始範圍全開, 數據範圍可行多了

```
                   | - - - - - - - |
                              | - - - - - - - |
| - - - - - - - |
x1              x2 x3         x5    x4        x6
```

並且一樣我們將segment tree每個節點都視為單點, 並且左閉右開(相鄰方塊不疊加)

例如. 上圖最上層方塊落下, 範圍[x3, x4], 實際上我們只影響[x3, x4-1] or [x3, x4) 左閉右開形式
對於這些左右端點, 全落下後就會像是skyline problem, 我們可以先列出這些點
然後將每個端點都對應到一個節點, 所以我們利用**pos2idx**去做端點與節點的一一對應: `pos2idx[position] = segment_tree_node_idx`

```py
SET = set() # remove duplicates
for l, length in positions:
    r = l+length
    SET.add(l)
    SET.add(r)
squares = list(sorted(SET))

pos2idx = {}
for idx, pos in enumerate(squares):
    pos2idx[pos] = idx
```

那再來就是建構出含有這些端點位置的segment tree, 並持續找出每個落下方塊時的`currMaxHeight`並更新
會發現邏輯上跟維護interval的方式是差不多的

```py
root = LazySegmentTreeMax(0, len(pos2idx)-1, 0)

res, currMaxHeight = [], 0
for l, length in positions:
    x1 = pos2idx[l]
    x2 = pos2idx[l+length]

    h = root.queryRange(x1, x2-1)
    h += length

    root.updateRange(x1, x2-1, h)
    currMaxHeight = max(currMaxHeight, h)
    res.append(currMaxHeight)
return res
```