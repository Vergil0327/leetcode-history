# Intuition

由於我們只關心能不能被k整除, 因此可以先對values[i] %= k

首先觀察到的是:由於total sum可以被k整除, 那我們一定可以分成若干份可以被k整除的group
因此我們可以用post-order DFS從底部往上來看, 一但當前root node加上左右子樹後可以被k整除, 那我們就split+1

為啥不用preorder?
因為想到底下這個例子

```
   A
 B   C
D E
```
萬一sum(A+B+C)可以被k整除, 並且sum(D+E)也可被k整除
但如果我們是由上到下preorder的話, 我們會把B跟D&E切開, 但這時D, E就沒有連再一起了

但如果是由下到上post-order的話, 就可以持續查看當前的root node以及左右子樹的總和, 一但可以被k整除那我們就把當前這個子樹從原本的樹中split出來
由於題目保證total_sum%k == 0, total_sum減去一個可以被k整除的子樹後, 剩餘的節點勢必也還是一顆valid的樹
所以我們就繼續看能不能再繼續切分更多子樹出來即可

因此我們post-order DFS就返回兩個值

1. 目前為止整個子樹的和. 由於我們只關心能不能被k整除, 所以將當前的和對k取餘
2. 目前為止這顆子樹共有多少個合法split

一但當前的子樹和對k取餘數為0, 那就代表我們可以將當前這顆子樹split出來, 因此`split += 1`
            
```py
def dfs(node, prev):
    cur = values[node]
    split = 0
    for nei in graph[node]:
        if nei == prev: continue
        tot, cnt = dfs(nei, node)
        cur += tot
        split += cnt

    cur %= k
    if cur == 0:
        split += 1

    return cur, split

_, res = dfs(0, -1)
# res即為答案, 返回res即可
```

summary:

> If a leaf's value is divisible by k, we can safely separate it from the tree, thus, increasing the number of components. If not, it will be a part of its parent's component.