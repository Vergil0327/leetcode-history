# Intuition

這題在如果依照時間軸來看的話, 在同個時間`t`的情況下會有許多的小group
一但整個group裡面有人知道secret的話, 那整個group就都會知道
所以從這邊能知道:在同個時間點下的每個meeting, 我們可以用union-find來把他們分組
- 一但組內有人知道secret, 那整個group也會自動union在一起.
  - 這邊我們可以限制我們的union總是union到較小的那個祖先, 所以我們可以用`find(person)`是否等於`0`來判斷當前這個person知不知道secret
- 但如果組內沒人知道secret, 那麼我們要把這個group給拆回原狀

1. 所以一開始我們先對meetins以時間排序
2. 然後把同個時間內的所有人全部union在一起, 並同時紀錄當前這時間點有哪些人
```py
i = 0
while i < len(meetings):

    currRound = set()
    j = i
    while j < len(meetings) and meetings[j][2] == meetings[i][2]:
        x, y, _ = meetings[j]
        px, py = find(x), find(y)
        currRound.add(x)
        currRound.add(y)
        if px != py: # union to smaller parent
            if px <= py:
                parent[py] = px
            else:
                parent[px] = py
        j += 1

    i = j-1
    i += 1
```
3. 我們查看當前這時間點的所有人 (以記錄在currRound裡) 是否知情
   - 如果find(person) == 0, 代表知情, 可以把person加入到最終答案裡
   - 如果不知情, 那就拆開原狀 => parent[person] = person
```py
for x in currRound:
    px = find(x)
    if px == 0:
        res.add(x)
    else:
        parent[x] = x
```