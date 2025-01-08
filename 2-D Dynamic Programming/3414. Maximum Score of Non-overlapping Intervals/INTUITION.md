# Intuition

top-down dp比較好想, 每個點都有兩種選擇: pick 或 skip
然後遍歷整個interval並且最多選到4個, 所以可以先定義出:

`dfs(i, size): the maximum score and picked indices having size intervals considering first i elements`

base case:

```py
if size == 0 or i == len(intervals):
    return [0, []] # score, picked indices
```

那最後重點其實就是挑完當前interval[i]後, 該怎麼高效找到下一個合法的`interval[j]`, 讓下次遞歸決定要不要挑選

下個合法interval[j]必須是跟當前選擇non-overlapping
對於interval, 我們預先移除掉duplicate然後排序後, 可以用binary search去挑出下個合法`j`, 所以:

- skip: skipped = dfs(i+1, size)
- pick:
    - picked = dfs(j, size-1)
    - [picked[0] + intervals[i][2], picked[1][:] + [interval[i]]]
    - j = bisect_right(interval, (interval[i][1]+1,))
        - 至於這邊`interval[i][1]+1`為什麼還要再`+1`, 看一下這個example: intervals = [[1,1,1000000000],[1,1,1000000000],[1,1,1000000000],[1,1,1000000000]]
        - 是為了避免左右端點重合的情況, 不排除掉我們會一直選到同個點四次


