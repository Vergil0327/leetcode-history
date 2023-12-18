# Intuition

first thought:
use BFS find minimum step from box to target and record player's position at each move/push, and check if player can reach every push position

所以如果我們要推動箱子, 我們得檢查player能不能移動到該施力處
同時記得檢查player移動時, 箱子本身也是不可穿越障礙物

因此, 我們首先應該要有個主要的BFS來紀錄box移動的路徑以計算出我們應該推幾次才抵達終點
為了避免BFS重複走到相同位置, 除了以box_position為狀態外, 還要記錄當次player是站在哪個位置推的
所以我們用個`visited` hashset來紀錄當前的位置狀態`(box_position, player_position)`

再來如果next_box_pos = r+dr, c+dc
那麼next_player_pos = r-dr, c-dc

如此一來就能有個主要框架:
```py
push = 0
while queue:
    for _ in range(len(queue)):
        (r, c), player_pos = queue.popleft()

        if (r, c) == target:
            return push

        for dr, dc in dirs:
            row, col = r+dr, c+dc
            player_next = (r-dr, c-dc)

            if row < 0 or row >= m or col < 0 or col >= n: continue
            if player_next[0] < 0 or player_next[0] >= m or player_next[1] < 0 or player_next[1] >= n: continue
            if grid[row][col] == "#": continue
            if grid[player_next[0]][player_next[1]] == "#": continue

            if (row, col, player_next[0], player_next[1]) in visited:continue

            if check_player_reachable(player_pos, player_next, (r,c)):
                visited.add((row, col, player_next[0], player_next[1]))
                queue.append([(row, col), (r, c)])
    push += 1
return -1
```

再來對於每次box移動, 我們都用個helper func `check_player_reachable(cur_player_pos, next_player_pos, cur_box_pos)`檢查player能不能移動到所需位置

至於helper func `check_player_reachable`, 我們就一樣再用個BFS檢查看player能不能走到該位置即可, 傳入box_pos是因為此時box也是個無法穿越的障礙物
```py
def check_player_reachable(src, dst, box_pos):
    q = deque([src])
    seen = set()
    while q:
        i, j = q.popleft()
        if i == dst[0] and j == dst[1]: return True
        for di, dj in dirs:
            ii, jj = i+di, j+dj
            if ii < 0 or ii >= m or jj < 0 or jj >= n: continue
            if grid[ii][jj] == "#": continue
            if ii == box_pos[0] and jj == box_pos[1]: continue
            if (ii, jj) in seen: continue
            seen.add((ii, jj))
            q.append((ii, jj))
    return False
```