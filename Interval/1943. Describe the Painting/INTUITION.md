# Intuition

一開始想法是
每個segments[i] = [start, end, color]代表我們對[start, end)這段區間塗上color, 亦即這段區間全`+= color`
最後要求的是每個位置的總和並以區間的形式返回

區間sum的計算讓我們可以想到用diffrenece array先標記每個segments[i]所影響的位置, 亦即:
```py
diff = [0] * 100005
diff[segments[i][0]] += segments[i][2]
diff[segments[i][1]] -= segments[i][2]
```

全部segments標記完後, 最後我們可以用O(n)的時間一次更新完segments對paintings的加總

但這會遇到個問題: ex. segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
我們答案會是[[1, 7, 12], [7, 8, 0]], 排除掉color=0的部分會是[[1, 7, 12]]
但實際上答案為[[1,4,12],[4,7,12]], 因為前面是{5,7}, 後面是{1,11}並不一樣
所以如果我們最後將difference array一次更新完後再想挑出連續區間的話, 會將這兩種情況混為一談,所以這解法有缺陷
仔細看constraint會發現每個colori都是**unique**的, 所以即使區間和相等, 兩個區間也不等

所以我們必須區分出每個區間
首先一樣, 我們必須用difference array的概念標記出區間和的變化, 只是這次diff改用**hashmap**來標記
```py
diff = defaultdict(int)
for start, end, color in segments:
    diff[start] += color
    diff[end] -= color
```


有了之後我們一樣開始依序計算區間和, 到這邊都跟difference計算區間和是一樣的:
```py
prevStart = 0
for start in sorted(diff.keys()):
    diff[start] += diff[prevStart]
    prevStart = start
```

但由於這時我們用另外一個變數`prevStart`來儲存上一個區間的開頭, 並且由於colori都是unique的
所以開始塗抹下個區間時, 前個區間的start到現在這個區間的start的顏色就已經確定了

```
_______
   _________
l  r => [l,r,color]
   l   r => got next [l,r,color]
       l    r => got next [l,r,color]
```

所以這時我們答案就能加上[prevStart, currStart, color[prevStart]]
然後再更新:
diff[currStart] += diff[prevStart]
prevStart = currStart

```py
prevStart = 0
for start in sorted(diff.keys()):
    if diff[prevStart] > 0:
        res.append([prevStart, start, diff[prevStart]])
    diff[start] += diff[prevStart]
    prevStart = start
```