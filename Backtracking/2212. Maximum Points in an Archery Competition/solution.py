class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        n = len(aliceArrows)
        self.res = [0, []]
        def dfs(state, i, remainArrows, points):
            if i == n:
                state[0] += remainArrows

                self.res[0] = max(self.res[0], points)
                if self.res[0] == points:
                    self.res[1] = state.copy()

                state[0] -= remainArrows # backtracking
                return
            
            dfs(state, i+1, remainArrows, points)

            state[i] = min(remainArrows, aliceArrows[i]+1)
            dfs(state, i+1, remainArrows-state[i], points+i if state[i] > aliceArrows[i] else points)
            state[i] = 0
        dfs([0]*n, 0, numArrows, 0)

        return self.res[1]