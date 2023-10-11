# Intuition

*這題最重要的核心概念是, 我們得主動設個合理的停損點來停止開放區域的BFS搜索*

無法escape的情況是blocked[i]從中隔開
1. blocked[i]連成一道牆, 並且牆的兩端與邊界相連
2. blocked[i]首尾相連把source或target包圍

source = [x,y]

最小的牆就是由四個方向組成的[[x-1,y], [x+1,y], [x,y-1], [x,y+1]]
再來就在往外四個方向
```
 A
AXA
 A

  A
 A A
A X A
 A A
  A
```

由於`0 <= blocked.length <= 200`, 所以分成兩種情況:

1. 目標很遠: 如果從source出發, 直到len(blocked)已不夠包圍時, 代表我們可以成功抵達target, 返回True
2. 目標很近: 如果我們BFS可以直接抵達目的地, 那返回True

因此想法是我們從source出發進行BFS, 所有BFS經過的visited cell會是個矩形
如果無法抵達, 代表blocked[i]是矩形的周長, 包圍著所有BFS-visited cells
如果可以抵達, 代表我們的BFS-visited cells超過blocked[i]所能包圍的數目

在blocked.length <= 200的情況下, 我們就抓個最糟糕情況
worst_area = len(blocked) * len(blocked) / 2

若要更精準一點的話, 其實可以想到能圍出的最大面積就是blocked跟兩側邊界所圍出的直角三角形
```
OOOOOOOX
OOOOOOX
OOOOOX
OOOOX
OOOX
OOX
OX
X
```
所以worst_area = 200 * (200-1) / 2 = len(blocked) * (len(blocked)-1) / 2
blocked[i] <= 200 => 兩百行

由於可能圍住source或target, 所以我們兩個都要檢查
只有兩個都沒被圍住, 才能抵達
