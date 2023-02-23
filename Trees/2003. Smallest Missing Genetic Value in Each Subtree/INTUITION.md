# Intuition

首先我們知道的是，只要子樹不包含`1`，那麼最小的missing number就是1

所以我們可以把我們的最終答案`res[i]`全部賦值為1
`res = [1] * n`

然後我們找出node value為1的node，如果不存在代表整棵樹的每個節點最小missing number都是1

```py
node1 = -1
for node, num in enumerate(nums):
    if num == 1:
        node1 = node
        break
if node1 == -1: return res
```

然後沿著node1往父節點走，把res[i]在重新設為0
```py
node = node1
res[node] = 0
while parents[node] != -1:
    res[node] = 0
    node = parents[node]
res[node] = 0
```

我們需要額外求smallest missing number的，就是這一條路徑上的每個節點

所以我們可以一樣再次沿著node1往上走，把每個節點底下的子節點全部加入到hashset裡，然後找smallest missing number

```py
node = node1
missing = 1
while node != -1:
    dfs(node, node)
    while missing in has:
        missing += 1
    res[node] = missing
    node = parents[node]
return res
```

把子節點加入到hashset也很簡單，用個preorder dfs持續把每個nums[node]加入到hashset裡即可

要注意的是，如果子節點已存在於hashset裡的話，代表這整個子樹我們之前就已經遍歷過了，可以直接return

>因為我們是從node1由下往上找回根節點的，所以不用再重新找一次之前經過的每個節點的子樹hashset

```py
has = set()
def dfs(node, prev):
    if nums[node] in has: return

    has.add(nums[node])
    for nei in children[node]:
        if nei == prev: continue
        dfs(nei, node)
```
