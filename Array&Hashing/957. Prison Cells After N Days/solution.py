class Solution:
    def prisonAfterNDays(self, cells, N):
        state = 0
        for i in range(8):
            if cells[i] == 1:
                state ^= 1 << i

        def change(state):
            nxt = 0
            for i in range(1, 7):
                if ((state>>(i-1))&1) == ((state>>(i+1))&1):
                    nxt |= 1 << i
            return nxt
        
        seen = {state: N}
        while N:
            seen.setdefault(state, N)
            N -= 1

            state = change(state)

            if state in seen:
                N %= seen[state] - N

        res = []
        for i in range(8):
            res.append((state>>i)&1)
        return res
