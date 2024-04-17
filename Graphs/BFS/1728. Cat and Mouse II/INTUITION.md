# Intuition

這題有可能和局 => 不能用DFS來遞歸搜索可能狀態
和局情況: 例如F被牆壁包圍, 然後貓跟老鼠互相維持一定速率追趕

所以就只能考慮用BFS嘗試搜索出全部狀態

而且這題比較特別的是: **我們得從最終狀態反推回來判斷**
我們關注三種狀態(mousePos, catPos, turn), 而最終狀態只可能是:
1. (mousePos, food, turn): cat in food position => cat wins
2. (food, catPos, turn): mouse in food position => mouse wins
3. (catPos, catPos, turn): mouse in cat position => cat catch mouse => cat wins

那麼我們就從這三種最終狀態往回推: (mousePos, catPos, turn) -> (mousePos', catPos', turn')

1. 如果(mousePos', catPos', turn')必須贏
   - 分情況討論
   - 如果(mousePos, catPos, turn)是mouse turn, cat wins的話 => (mousePos', catPos', turn')會是cat turn, 然後也必須贏
   - 如果(mousePos, catPos, turn)是cat turn, mouse wins的話 => (mousePos', catPos', turn')會是mouse turn, 並且也必須贏
2. 如果(mousePos', catPos', turn')必須輸
   - 一樣分情況討論
   - 再下個所有可能狀態(mousePos'', catPos'', turn''), 如果是cat turn, 並且cat wins的話 => 那代表(mousePos', catPos', turn')會是mouse turn並且必輸
   - 如果所有的(mousePos'', catPos'', turn'')都是mouse turn並且mouse wins的話 => 代表(mousePos', catPos', turn')會是cat turn並且必輸
   - 如果有任何一回合 (mousePos'', catPos'', turn'') 是平手, 那麼(mousePos', catPos', turn')就不會是必輸
3. 注意當輪次超過1000時, 老鼠還沒贏的話, 算老鼠輸

推薦觀看[@HuifengGuan](https://www.youtube.com/watch?v=ZDHb58kJFl0&ab_channel=HuifengGuan)的影片說明


# Approach

先找出最終狀態:

```py
memo = defaultdict(int) # (mouse row, mouse col, cat row, cat row, turn)
m, n = len(grid), len(grid[0])

cat, mouse, food = [], [], [] # positions of cat, mouse and food
for i in range(m):
    for j in range(n):
        if grid[i][j] == "F":
            food = [i,j]
        if grid[i][j] == "C":
            cat = [i,j]
        if grid[i][j] == "M":
            mouse = [i,j]

MOUSE, CAT = 1, 2
queue = deque()
for i in range(m):
    for j in range(n):
        if grid[i][j] == "#": continue
        if i == food[0] and j == food[1]: continue
        memo[i,j,food[0],food[1],MOUSE] = CAT # mouse turn, cat wins
        queue.append((i,j,food[0],food[1],MOUSE))

        memo[food[0],food[1],i,j,MOUSE] = MOUSE # mouse turn, mouse wins
        queue.append((food[0],food[1],i,j,MOUSE))
        
        memo[i,j,food[0],food[1],CAT] = CAT # cat turn, cat wins
        queue.append((i,j,food[0],food[1],CAT))
        
        memo[food[0],food[1],i,j,CAT] = MOUSE # cat turn, mouse wins
        queue.append((food[0],food[1],i,j,CAT))
```

然後BFS往回推:

```py
step = 0
while queue:
    step += 1
    if step > 2000: return False

    for _ in range(len(queue)):
        mi, mj, ci, cj, t = queue.popleft()
        status = memo[mi, mj, ci, cj, t]

        for mii, mjj, cii, cjj, tt in findNextStates(mi, mj, ci, cj, t):
            if memo[mii, mjj, cii, cjj, tt] != 0: continue

            # 如果status=CAT, 而tt又等於CAT, 代表是cat turn, cat wins, 同理如果status=MOUSE, 那就是mouse turn mouse wins
            # 所以這行一次涵蓋了兩種必贏的可能
            if tt == status:
                memo[mii, mjj, cii, cjj, tt] = status # 也是必贏
                queue.append((mii, mjj, cii, cjj, tt))
            elif allNextStatesWin(mii, mjj, cii, cjj, tt): # 必輸可能性
                memo[mii, mjj, cii, cjj, tt] = MOUSE if tt == CAT else CAT # 看這輪`tt`是誰的回合, 誰回合就誰輸, cat turn =>  mouse win
                queue.append((mii, mjj, cii, cjj, tt))

# 最後就看起始狀態老鼠會是贏還輸
return memo[mouse[0], mouse[1], cat[0], cat[1], 1] == MOUSE
```