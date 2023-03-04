# Intuition

看第一個例子，我們可以發現當我們從一個root轉移到另一個root時，只會有一個更動
例如從root0到root1, guess會從`[0,1]`變`[1,0]`

guess的變化可以輕易算出來，因此從這可以聯想到經典算法: ReRoot

```
當root = 0: [0,1], [1,2], [1,3], [2,4]
當root = 1: [1,0], [1,2], [1,3], [2,4]
當root = 2: [1,0], [2,1], [1,3], [2,4]
當root = 3: [1,0], [2,1], [3,1], [2,4]
當root = 4: [1,0], [2,1], [3,1], [4,2]
```

首先我們先任意選一個作為根，然後計算他有多少個正確的guess

```py
guessSet = set([(u, v) for u, v in guesses])
        
self.correct = 0
def dfs(node, parent):
    if (parent, node) in guessSet:
        self.correct += 1

    for nei in graph[node]:
        if nei == parent: continue
        dfs(nei, node)    
dfs(0, -1)
```

再來我們在進行一次DFS來reroot，查看每個節點作為根節點時的guess為多少，只要guess至少為k即可更新答案
最後答案為答案

```py
self.res = 0
def reroot(node, parent, correct):
    if correct >= k:
        self.res += 1
        
    for nei in graph[node]:
        if nei == parent: continue
        shift = 0
        if (node, nei) in guessSet:
            shift -= 1
        if (nei, node) in guessSet:
            shift += 1
        reroot(nei, node, correct+shift)
reroot(0, -1, self.correct)
```

這裡要注意的是，不可以寫成下面這種形式
比賽時這樣寫，結果缺沒注意這樣下個iteration的correct會是錯誤的
不然就是要backtracking correct

```py
def reroot(node, parent, correct):
    if correct >= k:
        self.res += 1
        
    for nei in graph[node]:
        if nei == parent: continue
        
        if (node, nei) in guessSet:
            correct -= 1
        if (nei, node) in guessSet:
            correct += 1
        reroot(nei, node, correct)
```