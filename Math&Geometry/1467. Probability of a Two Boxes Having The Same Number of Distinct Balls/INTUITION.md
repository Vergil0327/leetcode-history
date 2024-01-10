# Intuition

用dfs找出所有合法的分配方式, 利用backtracking or dp並記錄在`total`
並順便從合法分配方式中找出成功分配的方法數, 紀錄在`same`
兩者相除即為所求機率: same / total

分配方式很簡單, 用dfs簡單模擬一下即可
backtracking的話會是 O(6^8) = 1679616 => 約為10^6 級別 (可接受)

```py
self.total = self.same = 0
box1, box2 = defaultdict(int), defaultdict(int)
def dfs(i, box1, box2):
    if i == k:
        numBall1 = sum(box1.values())
        numBall2 = sum(box2.values())
        if numBall1 != numBall2: return

        # TODO
        self.total += ?
        self.same += ?

        return
    for c in range(balls[i]+1):
        box1[i] += c
        box2[i] += balls[i]-c
        dfs(i+1, box1, box2)
        box1[i] -= c
        box2[i] -= balls[i]-c

dfs(0,box1, box2)

return self.same / self.total
```

問題是該機率要怎麼求?

這題要找的是所有平均分配的排列, 例如 example2. [2,1,1]

總共有四顆球: [1A, 1B, 2, 3]去平均分配成兩堆, 所以總共的排列(permutation)為:

[1A,1B / 2, 3] => 該排列的組合數: C(balls[1], 2)
[1A,2 / 1B, 3] => 該排列的組合數: C(balls[1], 1) * C(balls[2], 1)
...

所以我們用dfs求出所有合法組合`[box1 / box2]`後, 在計算當前的排列方法數即為合法的方法數

首先先決條件是`box1裡球的總數 == box2裡球的總數 == n`
再來, 總方法數就 `total += sum(C(balls[i], box1[i]) for i in box1)`
那麼如果兩邊box的number of distinct相同, 就是成功的分配:
`same += sum(C(balls[i], box1[i]) for i in box1) if distinct(box1) == distinct(box2)`