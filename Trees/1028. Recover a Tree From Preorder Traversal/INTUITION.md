# Intuition

想法是先透過iterative的方式，把每個TreeNode依照preorder的順序存起來，然後再用dfs重新建構回來


首先一個while-loop來處理 `s`
首先開頭的`-`代表層數，我們可以處理掉同時記錄起來目前這個TreeNode是第幾層
```py
d = 0
while d < len(s) and s[d] == "-":
    d += 1
s = s[d:]
```

再來一個while-loop來找TreeNode的value:
```py
i = 0
while i < len(s) and s[i] != "-":
    i += 1
root = TreeNode(s[:i])
s = s[i:]
```

然後我們把每個TreeNode存在一個deque裡，之後會用到
```py
nodes = deque()
while s:
    d = 0
    while d < len(s) and s[d] == "-":
        d += 1
    s = s[d:]

    i = 0
    while i < len(s) and s[i] != "-":
        i += 1
    root = TreeNode(s[:i])
    nodes.append([root, d])
    s = s[i:]
```

等到我們處理完，得到所有TreeNode後，由於這個deque存的是preorder的順序，因此我們也利用一個preorder DFS來還原

首先第一個node為root node, 我們可以先取出來:
`root, depth = nodes.popleft()`

之後preorder DFS框架為:

```py
root, depth = nodes.popleft()
def dfs(root, d):
    # Base Case here

    dfs(root.left, d+1)
    dfs(root.right, d+1)

dfs(root, depth)
return root
```

nodes存的是preorder順序，所以我們照順序取出來即可
- 首先先把遞歸處理左子節點，如果nodes裡有節點，並且節點是當前的子節點即取出(我們可以透過先前儲存的層數來判斷是不是子節點)
- 等到沒有任何左子節點後，就改處理右子節點，一樣遞歸處理
- 那遞歸的base case很理所當然的:
  - 當nodes為空時，返回None
  - 當nodes為空時，我們會把`root=None`丟進遞歸，所以當root為空時，也直接返回None

```py
root, depth = nodes.popleft()
def dfs(root, d):
    if not root: return root
    if not nodes: return None

    if nodes and nodes[0][1] == d+1:
        root.left = nodes.popleft()[0]
    dfs(root.left, d+1)

    if nodes and nodes[0][1] == d+1:
        root.right = nodes.popleft()[0]
    dfs(root.right, d+1)
```

但其實我們僅在root.left跟root.right有數值的情況再遞歸即可:

```py
root, depth = nodes.popleft()
def dfs(root, d):
    if not nodes: return None

    if nodes and nodes[0][1] == d+1:
        root.left = nodes.popleft()[0]
        dfs(root.left, d+1)

    if nodes and nodes[0][1] == d+1:
        root.right = nodes.popleft()[0]
        dfs(root.right, d+1)
```