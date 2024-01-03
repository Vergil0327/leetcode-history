class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        nxt = [-1]*10
        offset = [0]*10
        removed = [0]*n

        for i in range(n):
            if nxt[int(num[i])] == -1:
                nxt[int(num[i])] = i

        res = list(num)
        for i in range(n):
            for d in range(10):
                if nxt[d] == -1: continue
                swap = nxt[d] + offset[d] - i
                if swap <= k:
                    res[i] = str(d)

                    # updates
                    k -= swap
                    removed[nxt[d]] = 1
                    for digit in range(10):
                        if nxt[digit] < nxt[d]:
                            offset[digit] += 1

                    start = nxt[d]+1
                    nxt[d] = -1
                    for j in range(start, n):
                        if removed[j]:
                            offset[d] -= 1
                        elif num[j] == str(d):
                            nxt[d] = j
                            break
                    break
        return "".join(res)