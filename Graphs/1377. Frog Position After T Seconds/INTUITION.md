# Intuition

這題很直覺的想到用DFS來模擬青蛙跳躍

首先我們先找出adjacency list `graph`
```py
graph = defaultdict(set)
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)
```

再來由於我們要求的是在`t`秒後, 青蛙停在`target`節點的機率

因此我們每次DFS先找出我們當前有多少個節點可以選擇, 機率就是 `1/len(choices)`

同時這邊要特別注意, 只要看到除法必須確認分母不可為零(避免division zero error)

```py
choices = []
for nei in graph[node]:
    if nei in visited: continue
    visited.add(nei)
    choices.append(nei)
prob = 1/len(choices) if choices else 0
```

再來就是一般的DFS
由於我們要判斷`t`秒後在不在`target`, 所以紀錄我們的step來判斷秒數
```py
def dfs(node, step):
    # count choices
    choices = []
    for nei in graph[node]:
        if nei in visited: continue
        visited.add(nei)
        choices.append(nei)
    prob = 1/len(choices) if choices else 0

    if node == target:
        # TODO

    res = 0
    for nei in choices:
        res = max(res, dfs(nei, step+1) * prob)
        
    return res
```

這題主要要特別注意的是**base case**

由於這題有說青蛙不可跳到訪問過的節點, 代表不能往回跳
所以我們要找的在`t`秒後停在target的機率, 有兩種可能
1. 在`t`秒時剛好就在`target`節點
2. 在`t`秒前已經抵達`target`同時沒有其他節點可以跳躍

```py
if node == target:
    if len(choices) == 0:
        return 1 if step <= t else 0
    return 1 if step == t else 0

# or
if node == target:
    if step > t: return 0
    if step == t: return 1
    return 1 if len(choices) == 0 else 0
```