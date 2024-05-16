class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        MOUSE, CAT = 1, 2  # turn
        game = defaultdict(int)  # (cat-pos, mouse-pos, turn): who wins

        queue = deque()
        for pos in range(1, len(graph)):
            for turn in [MOUSE, CAT]:
                # once mouse reaches hole, mouse wins
                game[pos, 0, turn] = MOUSE
                queue.append([pos, 0, turn])

                # once CAT catches MOUSE, cat wins
                game[pos, pos, turn] = CAT
                queue.append([pos, pos, turn])

        def findPrevStates(cat_pos, mouse_pos, turn):
            if turn == CAT:  # time for mouse to move in previous turn
                return [[cat_pos, prev_pos, MOUSE] for prev_pos in graph[mouse_pos]]
            else:  # time for cat to move
                return [
                    [prev_pos, mouse_pos, CAT] for prev_pos in graph[cat_pos] if prev_pos != 0
                ]  # cat can't reach hole

        def allNextStatesWin(cat_pos, mouse_pos, turn):
            """
            如果對手有任何一個情況沒贏, 那麼該輪次就不會是必輸
            如果對手全贏(allNextStatesWin), 那代表輸定了
            """
            if turn == MOUSE:
                for nxt in graph[mouse_pos]:
                    if game[cat_pos, nxt, CAT] != CAT:
                        return False
                return True
            else:  # CAT turn: 任一老鼠沒贏的話, 貓就不會輸
                for nxt in graph[cat_pos]:
                    if nxt == 0: continue
                    if game[nxt, mouse_pos, MOUSE] != MOUSE:
                        return False
                return True

        while queue:
            for _ in range(len(queue)):
                cat, mouse, turn = queue.popleft()
                status = game[cat, mouse, turn]

                for prev_cat, prev_mouse, prev_turn in findPrevStates(cat, mouse, turn):
                    if game[prev_cat, prev_mouse, prev_turn] != 0: continue  # already has result

                    # 當輪次老鼠輪次, 代表前個輪次是貓行動, 如果當輪次貓贏 => 代表前個狀態仍是貓贏 鼠亦同理.
                    # 或者說:當輪次貓贏, 前個輪次貓動, 那前個輪次的下個狀態既然是貓贏, 那前個輪次肯定也是貓贏
                    if status == prev_turn: 
                        game[prev_cat, prev_mouse, prev_turn] = status
                        queue.append([prev_cat, prev_mouse, prev_turn])

                    elif allNextStatesWin(prev_cat, prev_mouse, prev_turn):  # 如果沒贏, 那考慮確定是輸的情況 => 如果下個輪次對手都贏, 那這輪必輸
                        game[prev_cat, prev_mouse, prev_turn] = MOUSE if prev_turn == CAT else CAT
                        queue.append([prev_cat, prev_mouse, prev_turn])
        return game[2, 1, 1]  # intial state: cat at 2, mouse at 1, mouse turn