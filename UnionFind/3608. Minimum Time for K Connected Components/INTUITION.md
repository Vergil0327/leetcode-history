# Intuition

時間`t`越大, 移除的edges越多, disconnected components越多
時間`t`越小, 移除的edges越少, disconnected components越少

=> 單調性 => binary search `t`

所以我們主框架為:

```py
def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
    l, r = 0, 10**9

    while l < r:
        t = l + (r-l)//2

        if count(t) >= k:
            r = t
        else:
            l = t+1
    return l
```

那麼helper function `count` 就透過union-find找出所有`timei > t`的connected component數目即可

# Optimized

這題還有個更好的解法是**逆向思考**

首先依照時間由大到小排序, 全部edges都移除的話會有`n`個disconnected components
我們倒著算回來, 從時間最晚的邊逐漸將節點連接再一起, 每成功連接一個, connected componenets數目就少一個

直到connected componenets的數目`小於k`時, 這時的時間即為所求的最小時間
因為這時候是剛好為`k`個connected component的時間

這樣就可以省略掉binary search

```py
def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
    if not edges: return 0
    edges.sort(key = lambda e: -e[2])
    f = [i for i in range(n)]

    def find(x):
        if x == f[x]:
            return x
        f[x] = find(f[x])
        return f[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        f[x] = y
        return True

    count = n
    for u, v, t in edges:
        if union(u, v):
            count -= 1
        if count < k:
            return t
    return 0
```