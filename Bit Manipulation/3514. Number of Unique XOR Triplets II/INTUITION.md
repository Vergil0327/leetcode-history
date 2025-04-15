# Intuition

對於nums[i]來說, 我們可以預先計算它的合法`nums[j] XOR nums[k]` pair

```py
arr = []
for i in range(n-1, -1, -1):
    pairs = set()
    for j in range(i, n):
        pairs.add(nums[i]^nums[j])
    arr.append(pairs)
```

然後再將合法pairs跟nums[i]進行XOR即可, 分開進行下的時間複雜度為O(n^2)

```py
for i in range(n-1, -1, -1):
    for p in arr[i]:
        res.add(p^nums[i])
```

但看了一下會發現其實我們可以合併循環, 變成:

```py
n = len(nums)

res = set()
pairs = set()
for i in range(n-1, -1, -1):
    for j in range(i, n):
        pairs.add(nums[i]^nums[j])

    for p in pairs:
        res.add(p^nums[i])

return len(res)
```

### Edge Case

在**n<3**時, 因為會有重複的elements, 所以distinct XOR只會有n個
ex. `[1,2]` => `{1,1,2}`, `{1,2,2}`, `{1,1,1}`, `{2,2,2}`, ...