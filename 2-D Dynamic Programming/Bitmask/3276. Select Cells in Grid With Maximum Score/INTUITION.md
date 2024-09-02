
# Intuition

首先將全部數值挑出來變成1-D array, 然後利用top-down dp以**pick-or-skip**策略來挑找出最佳解
並且由於`1 <= grid.length, grid[i].length <= 10`, 所以我們可以用bitmask來表示我們row的選擇狀態

定義:
dp(i, row_state, value_state): the maximum score considering i-th round and use bitmask `row_state` for finished rows and value_state in 7-base value for picked values

那這樣相當於我們用`row_state`紀錄了我們已經確定挑完的rows, 並且將所有挑過的數都以7進制紀錄在value_state裡

```py
def maxScore(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    arr = []
    for i in range(m):
        for j in range(n):
            arr.append([grid[i][j], i, j])
    arr.sort(reverse=True)

    size = len(arr)
    shift = 3
    base = 7

    @cache
    def dfs(i, row_state, value_state):
        if row_state.bit_count() == m: return 0
        if i >= size: return 0

        res = dfs(i+1, row_state, value_state) # skip
        
        num, row, col = arr[i]
        if (row_state>>row)&1 == 0:
            new_row_state = row_state | (1<<row)
            
            picked = set()
            tmp = value_state
            b_cnt = row_state.bit_count()
            k = pow(base, shift)
            for _ in range(b_cnt):
                picked.add(tmp % k)
                tmp //= k

            if num not in picked:
                new_value_state = value_state * k + num
                res = max(res, dfs(i+1, new_row_state, new_value_state) + num)
        return res

    return dfs(0, 0, 0)
```

但可惜這樣會 MLE (memory limit exceeded)

所以我們需要進一步優化程式碼
但其實我們作法已經很接近了

我們將整個grid化作1-D array, [grid[i][j], i], 後由大到小排序
同樣用skip-or-pick策略進行top-down dp

- 對於當前arr[i]可以選擇不選
- 對於當前arr[i]可以選, 但前提是先前沒有選過相同row的數值
    - 那在選了之後, 我們我們就移動指針`i`, 跳過所有重複數值的arr[i]

如此一來我們就能不需要紀錄我們先前選過哪些數值來避免選到重複

time: O(m*n * 2^m) 
space: O(m*n * 2^m) 