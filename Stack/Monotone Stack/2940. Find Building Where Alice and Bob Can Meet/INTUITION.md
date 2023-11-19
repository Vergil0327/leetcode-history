# Intuition

找出符合heights[idx] >= max(heights[queries[i][0]], heights[queries[i][1]]), 且idx >= max(queries[i][0], queries[i][1])的最小idx


如果在queries[i]中, 靠左index為`l`, 靠右為`r`, 那麼:
- if heights[r] > heights[l] or l == r, res[i] = r
- else, 在[r+1, n)這範圍內找出最小`idx`使得heights[idx] > heights[l]

如果我們將queries對`r`由大到小進行排序組成`arr`, 其中:
**arr[i] = [r, l, index] where r = max(a, b), l = min(a, b)**

那麼我們在遍歷queries過程中, 我們就能持續將所有index > r的heights[index]都加進一個集合裡

```
heights X X X X X X X {X X X}
            l       r 
```
在{X X X}這集合中, 由於我們要的是最靠左且heights[index] > heights[l]的位置, 所以我們維護一個單調遞增的stack

j從len(heights)-1開始, 從後往前遍歷所有j > r的heights[j], 一旦heightsj >= monostack[0][0], 代表我們找到一個更好的height, 那我們就能將monostack裡更靠右且數值小於等於heights[j]的全部pop掉
```py
j = len(heights)-1
monostack = deque()
while j > r:
    while monostack and monostack[0][0] <= heights[j]:
        monostack.popleft()
    monostack.appendleft([heights[j], j])

    j -= 1
```

這樣我們就能在這個單調遞增的stack裡, 利用binary search `index = bisect_right(monostack, heights[l], key=lambda x:x[0])`
找出最靠左且heights[index] > heights[l]的值