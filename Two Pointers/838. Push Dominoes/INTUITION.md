# Intuition

想到two pointers
只要dominoes[i]是"L"或"R", 我們就試著推推看
- 如果是"L": 將所有"."往左推, 如果遇到"R", 那就是將這段"....."從左右端點持續往中間推, 如果沒遇到反方向的力, 那就是全部變成"L"
- 如果是"R": 將所有"."往右推, 如果遇到"L", 也一樣將這段"....."從左右端點持續往中間推, 如果沒遇到反方向的力, 那就是全部變成"R"

這樣下來, 所有的"..."最多只會被重複處理兩次, 一開始遇到"R"往右推一次, 後面再遇到"L"在往左確認一次


所以我們分三個部分:

- 如果dominoes[i]==".": 直接放入我們的stack裡
- 如果dominoes[i]=="R": 開始往右推相接的"."
    - 如果一路推到底或是遇到下個"R", 那就是全部"."都被推成"R"
    - 但如果最後遇到"L", 那就是這段區間雙指針往中心推倒, 變成"...RRR(.)LLL..."
- 如果dominoes[i]=="L": 同上概念, 開始往左推鄰近的"."

time: O(n)
space: O(n)

## Optimized

綜合上述, 其實就是處理以下各個區間:
1. "L...L": 將所有".", 推成"L"
2. "R...R": 將所有".", 推成"R"
3. "L...R": 中間"."不受影響
4. "R...L": 兩側網中心推倒

為了最左右兩端方便計算區間, 兩側各加上`"L"`, `"R"`

```py
def pushDominoes(self, dominoes):
    dominoes = 'L' + dominoes + 'R'
    res = ""
    i = 0
    for j in range(1, len(dominoes)):
        if dominoes[j] == '.':
            continue
        middle = j - i - 1
        if i:
            res += dominoes[i]
        if dominoes[i] == dominoes[j]:
            res += dominoes[i] * middle
        elif dominoes[i] == 'L' and dominoes[j] == 'R':
            res += '.' * middle
        else:
            res += 'R' * (middle / 2) + '.' * (middle % 2) + 'L' * (middle / 2)
        i = j
    return res
```