# Intuition

由於1 <= nums[i] <= 50, 先找出每個nums[i]的coprime?
找出每個nums[i]的coprime紀錄在coprimes後, coprimes = {nums[i]: [coprime...]}

然後在進行dfs時, 在preorder DFS位置我們會知道當前node的所有ancestors
由於nums[i]數值很小, 我們可以利用前面建立的`coprimes`找出當前節點的所有coprime, 然後查看這個coprime有沒有在ancestors裡
我們要的就是深度最深的coprime ancestor的值

因此, 在preorder位置更新num2idx及ancestors, 並記得在post-order回溯進行backtracking
如此一來便能在一次DFS紀錄當前節點的ancestors並從coprime著手找出合適的ancestor, 找出其中level最深的一個

主要框架:
```py
def dfs(node, prev, level):
    num2idx[nums[node]].append(level)
    ancestors.append(node)

    for nei in graph[node]:
        if nei == prev: continue
        dfs(nei, node, level+1)

    # backtracking
    num2idx[nums[node]].pop()
    ancestors.pop()
```

搜索deepest coprime-ancestor
```py
idx = -1
for p in coprimes[nums[node]]: # 1 <= p <= 50
    if num2idx[p]:
        idx = max(idx, num2idx[p][-1])

if idx != -1:
    res[node] = ancestors[idx]
```