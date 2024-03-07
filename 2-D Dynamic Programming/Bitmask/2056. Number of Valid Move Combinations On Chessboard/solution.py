class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        dirs1 = [[0,1],[0,-1],[1,0],[-1,0]] # horizontal or vertical
        dirs2 = [[1,1],[1,-1],[-1,-1],[-1,1]] # diagnal

        destinations = []
        for p in pieces:
            if p == "rook":
                destinations.append(dirs1)
            elif p == "queen":
                destinations.append(dirs1 + dirs2)
            else: # bishop
                destinations.append(dirs2)

        def check(pos):
            occupied = set()
            for r, c in pos:
                occupied.add((r,c))
                if r <= 0 or r > 8 or c <= 0 or c > 8:
                    return False
            if len(occupied) < len(pos): return False

            return True

        self.res = set()
        def dfs(pos, dirmask, stop):
            if stop == 0: return # all stopped

            self.res.add(tuple(pos))

            for nxt_stop in range(1<<len(dirmask)):
                if stop & nxt_stop != nxt_stop: continue

                new_pos = pos.copy()
                for i in range(len(new_pos)):
                    did_stop = (nxt_stop>>i)&1
                    new_pos[i] = (new_pos[i][0] + dirmask[i][0]*did_stop, new_pos[i][1] + dirmask[i][1]*did_stop)

                if not check(new_pos): continue
                dfs(new_pos, dirmask, nxt_stop)

        positions = [tuple(p) for p in positions] # 為了能放進hashset, 我們把list轉成tuple
        for dirmask in product(*destinations):
            stop = (1<<len(pieces))-1
            dfs(positions, dirmask, stop)
        
        return len(self.res)
