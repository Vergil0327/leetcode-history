# Intuition


subseq..., arr[i]-arr[j], arr[j], arr[i]

arr[i]是由前兩項相加得出, 我們可以用top-down dp來嘗試每個arr[i]與另一個arr[j]來組成fibonacci-like subseq.

對於arr[i]來說, arr[j]可以任意選擇, 只要j滿足`i < j < n`且`arr[j] in arr`
那在選擇完arr[j]來後, 那後面的選擇就是固定的了:
`next = prev_choice + arr[i] where next in arr`

所以我們可以定義dfs返回longest length of fibonacci-like subseq.
並且根據上面式子, 我們dfs必須紀錄`(i, prev_choice)`來嘗試每個arr[i]為開頭組成的fibonacci-like subseq.

所以high-level框架為:
```py
res = 0
for i in range(n):
    res = max(res, dfs(i))
return res if res > 2 else 0
```
*note. 如果res <= 2, 代表組不成fibonacci-like subseq.*

由於我們要確認`next`跟`arr[j]`存不存在於arr裡, 所以我們還需要個hashmap
`hashmap = {v:i for i, v in enumerate(arr)}`
