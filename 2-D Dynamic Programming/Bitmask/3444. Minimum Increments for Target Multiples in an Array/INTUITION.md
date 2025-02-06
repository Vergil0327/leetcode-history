# Intuition

看向限制 `1 <= target.length <= 4`, 我們最多只需要考慮四個數的multiple
我們只能進行increment操作, 數值只能往上
一開始暫時沒想法, 先排個序, 依序考慮nums[i]

後來看了example2想到, 我們由大到小排序處理的話, 如果nums[i]能滿足target[j]的話, 我們還能後續查看target[j+1:]是不是也有剛好能滿足的
由於整個target.size <= 4, 所以我們可以用個bitmask來表示有哪些target[j]是已經處理好的

那這樣顯而易見的, 我們可以裡用bitmask + dynamic programming來試著處理這項問題

定義dfs(i, state): the minimum number of operations required so that target state has at least one multiple in nums[:i].

額外補充: 如果state = 0x1101, 代表第1,2,4個(1-indexed)target element都已經有multiple

那接下來就是我們主幹:

首先先排序並剔除duplicates
```py
target = list(set(target)) # remove duplicate

target.sort(reverse=True)
nums.sort(reverse=True)
```

再來就是我們的核心top-down dp with bitmask:

首先base case顯而易見:

1. 當我們處理好全部target[j], 也就是`state.bit_count() == len(target)`, 就能直接返回0
2. 當我們遍歷完整個nums, 如果處理好整個target, 那就返回0, 不然的話由於我們是要找minimum, 我們返回inf

那再來我們就採取take or skip
對於當前nums[i]我們可以選擇拿來滿足target[j], 也可以選擇跳過

那如果要選擇哪來滿足target[j]的話, 我們就得找出最靠近nums[i]的target[j] multiple
找到之後就能計算所需的操作數: `multiple - nums[i]`

那處理好將nums[i]轉成target[j]的multiple後, 我們得順便在往後檢查target[j+1:], 看有沒有剛好nums[i]也是multiple的

最後我們全部決策裡取一個最少所需操作數即為答案

```py
def dfs(i, state):
    if state.bit_count() == m: return 0
    if i >= n: return 0 if state.bit_count() == m else inf

    res = dfs(i+1, state)

    for j in range(m):
        if (state>>j)&1: continue # target[j] has already done
        
        x = ceil(nums[i]/target[j])
        multiple = target[j]*x

        inc = multiple - nums[i]
        newState = state | (1<<j)
        for k in range(j+1, m):
            if multiple % target[k] == 0:
                newState |= (1<<k)
        res = min(res, dfs(i+1, newState) + inc)
    return res
```