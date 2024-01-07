# Intuition

1. 最多26字母 => 我們用26-bitmask來表示當前prefix所包含的字母state
2. 最多可更換一次字符 => 用`change`表示已更換與否: True/False

那這樣我們能用bitmask + dfs (topdown dp)來搜索最多能分割成多少partition
根據上述分析, 我們需要3個state, 所以可以這麼定義dfs:
```
def dfs(i, state, change): the maximum partition considering first i elements when current prefix state is `state` and we've changed any index once
```

- 對於當前s[i]字符, 我們可以選擇換或不換, 換的話必須`change == False`
- 還有就是得檢查當前bitmask不是已經超過k個distinct character, 超過的話代表我們找到一個合法partition
    - 也就是確認bitmask.bit_count() > k這條件符合了沒, 符合的話那就可以partion+1, next_state變為1<<(ord(s[i])-ord("a"))
    - 如果還沒超過, 那就繼續往後找longest prefix, next_state = state | (1<<(ord(s[i])-ord("a")))

所以首先如果不換s[i]的話, 先判斷找到合法partition了沒:

1. 如果`next_state.bit_count() > k`: `dfs(i+1, 1<<bit, change)+1`
2. 如果`next_state.bit_count() <= k`: 繼續找longest prefix, `dfs(i+1, state | (1<<bit), change)`

```py
bit = ord(s[i])-ord("a")
new_state = state|(1<<bit)

if new_state.bit_count() > k:
    res = max(res, dfs(i+1, 1<<bit, change)+1)
else:
    res = dfs(i+1, new_state, change)
```

如果更換當前s[i]的話, 就遍歷最多26個與當前s[i]不同的字母, 進行狀態轉移, 一樣判斷next_state.bit_count()有沒有大於`k`:

```py
if not change:
    for j in range(26):
        if j == bit: continue
        new_state = state|(1<<j)
        if new_state.bit_count() > k:
            res = max(res, dfs(i+1, (1<<j), True)+1)
        else:
            res = max(res, dfs(i+1, new_state, True))
```