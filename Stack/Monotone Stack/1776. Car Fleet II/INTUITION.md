# Intuition

首先, 只要速度比前面快, 那就肯定能撞上
能先找出每台車會先跟前面哪台車第一次撞上

```py
n = len(cars)

stack = []
firstCollide = [-1]*n
for i in range(n):
    while stack and cars[stack[-1]][1] > cars[i][1]:
        firstCollide[stack.pop()] = i
    stack.append(i)
```

如果i-th車會撞到firstCollide[i] => car fleet
那對於i+1車:
如果firstCollide[i+1] = -1, 那代表他不會撞到任何一台車, 並且就算他後面的車撞到前面任何一台車形成car fleet, 他也不會相撞.
因為firstCollide[i+1] = -1時, 代表他的速度比前面任何一台都慢, 但比之前的快

那再來討論firstCollide[i] != -1的情況, 也就是會形成car fleet的情況
由於一開始位置已經由左到右排序, 或許應該從後往前來看
因為如果有複數台車都撞上同一台的話, firstCollide[i] == firstCollide[i+1] == firstCollide[i+2], 也是最靠後的那台先撞上

example 2:
前兩台車都會撞到第三台車, 一但第二台車撞上第三台, 兩台就會形成速度3的car fleet 
而之後第一台會撞到第二台車, 所以如果第一台前面還有一台車的話, 如果會撞到也是撞到第一台

所以這就想到monotonic stack, 我們能維護一個monotonic stack, 其中monotonic stack代表的是會被cars[i]撞到的car fleet最末端車
並且我們應該從後往前遍歷, 並且那些stack[-1].speed >= cars[i].speed的通通都撞不到, 都可以pop掉
那麼最後留下的就是會撞成car fleet的車, 我們就計算時間紀錄在res[i]上

```py
n = len(cars)

def calTime(car1, car2):
    pos1, spd1 = car1
    pos2, spd2 = car2
    return (pos2-pos1)/(spd1-spd2)

res = [-1]*n
stack = []
for i in range(n-1, -1, -1):
    pos, spd = cars[i]
    while stack and cars[stack[-1]][1] >= spd:
        stack.pop()
    if stack:
        res[i] = calTime(cars[i], cars[stack[-1]])
    stack.append(i)
return res
```

但這時會發現過不了這case:
cars=[[3,4],[5,4],[6,3],[9,1]]
Output: [3.00000,1.00000,1.50000,-1.00000]
Expected: [2.00000,1.00000,1.50000,-1.00000]

這邊會發現我們漏掉了一個可能性, 那就是:
對於cars[i]來說, stack[-1]這台車有可能在被cars[i]撞到之前就先撞到別人形成car fleet了
其中car fleet的速度會是最慢的那台, 不會是stack[-1]這台, 因此這時對於cars[i]來說, stack[-1]這台不再重要, 也要pop掉

我們看上面這test case
以0-indexed來說:
- cars[1]在1秒後會撞上cars[2]
- cars[2]在1.5秒後會撞上cars[3]

這時cars[0]在2秒後就會撞上(cars[1]+cars[2]+cars[3])中最慢的那台, 也就是cars[3]
而非3秒後撞上cars[2]

因此我們還必須加上一個條件, 把那些在cars[i]追到之前就已經先形成cars fleet的給pop掉:
`res[stack[-1]] > 0 and calTime(cars[i], cars[stack[-1]]) >= res[stack[-1]])`

這樣最終留在stack的cars[stack[-1]], 才是正確會跟cars[i]相撞形成car fleet的車

time: O(n)
space: O(n)