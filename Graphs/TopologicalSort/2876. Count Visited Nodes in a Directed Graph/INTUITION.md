# Intuition

n個節點有n條邊 => 必定至少會形成一個cycle

1. 對於處於cycle的所有節點, 他們的visited different nodes就是cycle本身的大小
2. 對於cycle以外的節點, 那就看他們路過多少節點再加上cycle大小

所以首先先找出cycle的大小以及處於cycle內的所有節點, 這樣所有在cycle內的節點的answer[i]為: cycle.size

我們可以用topological sort先找出`nodeInCycle`以及`nodeNotInCycle`
對於在cycle內的, 我們就找出他們的cycle size

```py
nodeInCycle = [node for node, deg in enumerate(indeg) if deg > 0]
for node in nodeInCycle:
  if res[node] != 0: continue

  cycle = set()
  while node not in cycle:
    cycle.add(node)
    node = edges[node]
  
  for node in cycle:
    res[node] = len(cycle)
```

對於不在cycle內的節點, 我們用dfs並在post-order位置更新他們的res[i]即可
dfs的base case則如前面討論所述：
if res[node] != 0, 代表該node位於cycle內, 此時就返回cycle size即可
=> `if res[node] != 0: return res[node]` 

```py
def dfs(node):
  if res[node] != 0: return res[node]

  res[node] =  dfs(edges[node])+1
  return res[node]

for node in nodeNotInCycle:
  dfs(node)
```