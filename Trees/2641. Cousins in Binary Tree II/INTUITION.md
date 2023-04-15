# Intuition

首先我們level by level來看

每一層的每個節點都以父節點作為一個group

```
example 1.
    {5}
  {1} {9}
{1,10}  {7}

    5
  1    9
1  10    7
```

如圖所示:
我們目標是把每個節點的值都換成`sum(cousin's value)`
如第三層為例:
- {1,10}的`sum(cousin's value)`等於`7`
- {7}的`sum(cousin's value)`等於`1+10`

而所謂的sum(cousin's value)其實也就是那層的總和減去自身這個group的值
所以:
- {1,10} 的`sum(cousin's value)`等於`1+10+7 - (1+10) = 7`
- {7} 的`sum(cousin's value)`等於`1+10+7 - (7) = 11`

所以我們可以先用BFS把每一層的總和算出來，紀錄在hashmap裡
`hashmap[level] = sum(nodes at level)`

然後我們就可以在BFS一遍

子節點是依據父節點來作為一個group, 所以我們在BFS遍歷時可以得出:

- 當前這個group的總和`SUM`為`node.left + node.right`

再來我們就能更新此時這個group的節點`node.left`跟`node.right`為`hashmap[level] - SUM`了

```py
while queue:
    for _ in range(len(queue)):
        node, level = queue.popleft()
        
        SUM = 0
        if node.left:
            SUM += node.left.val
            queue.append([node.left, level+1])
        if node.right:
            SUM += node.right.val
            queue.append([node.right, level+1])

        if node.left:
            node.left.val = total[level+1] - SUM
        if node.right:
            node.right.val = total[level+1] - SUM
```

另外由於前兩層是沒有cousin's node的, 所以我們可以直接賦值為`0`
```py
while queue:
    for _ in range(len(queue)):
        node, level = queue.popleft()
        
        if level <= 1:
            node.val = 0
```