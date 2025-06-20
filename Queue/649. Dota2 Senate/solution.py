from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # round-based procedure
        # until last one win
        
        ban = defaultdict(int)
        nxt = deque()
        cur = deque(senate)
        exists = {}
        while cur:
            while cur:
                party = cur.popleft()
                if party == "R" and ban["R"] > 0:
                    ban["R"] -= 1
                elif party == "D" and ban["D"] > 0:
                    ban["D"] -= 1
                else:
                    if party == "R":
                        ban["D"] += 1
                    else:
                        ban["R"] += 1

                    nxt.append(party)
                    exists[party] = True
            if len(exists) == 1:
                return "Radiant" if "R" in exists else "Dire"
            cur, nxt = nxt, deque()
            exists = {}

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r_idx = R.popleft()
            d_idx = D.popleft()

            if r_idx < d_idx:
                R.append(r_idx + n)
            else:
                D.append(d_idx + n)

        return "Radiant" if R else "Dire"