# Intuition
1. find connected groups
2. check edge in each group

# Complexity
- Time complexity:
$$O(n^2)$$

- Space complexity:
$$O(n^2)$$

# Other Solution

如果complete connected component有`n`個節點, 代表他的edges = n * (n-1) // 2
我們可以利用這個條件, 先把我們有的邊加入到每個connected component中

```py
edge = [0] * n
for u, v in edges:
    edge[find(u)] += 1
```

然後就可以用O(1)時間判斷是不是該connected component是不是complete

```py
groups = defaultdict(list)
for node in range(n):
    groups[find(parent[node])].append(node)

res = 0
for group in groups:
    n = len(groups[group])
    if edge[group] == n*(n-1)//2:
        res += 1
```
