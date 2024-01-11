# Intuition

最多26種字母可以選擇包含在該substring裡
[a...][b...][c...][d...]

我們遍歷a-z, 找出所有包含該字母的合法substring

合法substring必須包含所有字母的occurence
所以我們可以用hashmap先找出每個字母的index的左右端點: `index[ch] = [leftmost index, rightmost index]`

那這樣我們就能得到最多26字母的區間
再來我們遍歷每個字母, 找出如果能滿足包含當前字母的substring

做法是從index[ch]的左右端點開始, 如果裡面有包含其他字母, 就透過helper func `expand`持續延長左右端點
```py
index = defaultdict(list) # s[i]: [idx1, idx2, ...]
for i, ch in enumerate(s):
    index[ch].append(i)

valid = set()
for ch, (l, r) in index.items():
    length, substr = expand(ch, l, r)
    valid.add((length, substr))
```

等找出所有可能substring後, 以長度排序, 優先拿最短的substring即可 (greedy)
```py
res = []
arr = sorted(list(valid))
seen = set()
for _, substr in arr:
    SET = set(substr)
    if any(ch in seen for ch in SET): continue
    seen |= SET
    res.append(substr)

return res
```

那最關鍵的就是helper function `expand`

1. 遍歷s[l:r]的所有字母延展左右邊界 => 產生新的邊界[ll, rr]
2. 繼續遍歷[ll, l-1]跟[r+1, rr]的字母延展邊界
3. 直到無法再延展左右邊界

```py
# two pointers
def expand(ch, l, r):
    ll, rr = l, r
    seen = set([ch])
    for i in range(l, r+1):
        if s[i] in seen: continue
        seen.add(s[i])
        left, right = index[s[i]][0], index[s[i]][1]
        ll = min(ll, left)
        rr = max(rr, right)

    while l > ll or r < rr:
        nextL, nextR = ll, rr
        for i in range(ll, l):
            if s[i] in seen: continue
            seen.add(s[i])
            left, right = index[s[i]][0], index[s[i]][1]
            nextL = min(nextL, left)
            nextR = max(nextR, right)

        for i in range(r+1, rr+1):
            if s[i] in seen: continue
            seen.add(s[i])
            left, right = index[s[i]][0], index[s[i]][1]
            nextL = min(nextL, left)
            nextR = max(nextR, right)
        l, r = ll, rr
        ll, rr = nextL, nextR
    return r-l+1, s[l:r+1]
```


time: $O(n + 26 * O(expand))\text{ where }O(expand) = O(n)$
