# Intuition

想了一下DFS, 似乎沒辦法處理draw的情況, 所以直接往BFS去想

最終狀態有可能是:
1. 最終MOUSE贏的情況 => MOUSE reaches hole
2. 最終CAT贏的情況 => CAT catches MOUSE

所以我們知道最終確認輸贏的狀態為:
```py
for pos in range(1, len(graph)):
    for turn in [MOUSE, CAT]:
        # once mouse reaches hole, mouse wins
        game[pos, 0, turn] = MOUSE
        queue.append([pos, 0, turn])

        # once CAT catches MOUSE, cat wins
        game[pos, pos, turn] = CAT
        queue.append([pos, pos, turn])
```

再來試著從最終結果往回推, 然後最後看一開始位置的狀態能不能確認是輸或贏
bottom-up的形式


那再來就討論如何往回推前個狀態是輸是贏

1. 如果前個狀態要贏:
   - 如果當前是貓贏: 找出前個狀態, 如果是貓的輪次, 那前個狀態肯定也是貓贏
   - 如果當前是鼠贏: 找出前個狀態, 如果是鼠的輪次, 那前個狀態肯定也是鼠贏
2. 如果前個狀態要輸:
   - 代表他未來的所有狀態都不可能贏

