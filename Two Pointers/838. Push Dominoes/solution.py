class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)

        i = 0
        res = []
        while i < n:
            if dominoes[i] == ".":
                res.append(dominoes[i])
                i += 1
            elif dominoes[i] == "R":
                res.append(dominoes[i])

                pushed = []
                j = i+1
                while j < n and dominoes[j] == ".":
                    pushed.append(".")
                    j += 1
                if j >= n or dominoes[j] == "R":
                    res.extend(["R"]*len(pushed))
                elif dominoes[j] == "L":
                    l, r = 0, len(pushed)-1
                    while l < r:
                        pushed[l] = "R"
                        pushed[r] = "L"
                        l, r = l+1, r-1
                    res.extend(pushed)
                i = j
            elif dominoes[i] == "L":
                pushed = []
                j = i-1
                while j >= 0 and res[-1] == ".":
                    pushed.append(res.pop())
                    j -= 1

                if j < 0 or dominoes[j] == "L":
                    res.extend(["L"]*len(pushed))
                elif dominoes[j] == "R":
                    l, r = 0, len(pushed)-1
                    while l < r:
                        pushed[l] = "R"
                        pushed[r] = "L"
                        l, r = l+1, r-1
                    res.extend(pushed)

                res.append(dominoes[i])
                i += 1
        return "".join(res)
    

# Optimized
class Solution:
    def pushDominoes(self, dominoes):
        dominoes = 'L' + dominoes + 'R'

        res = ""
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue
            middle = j - i - 1
            if i:
                res += dominoes[i]
            if dominoes[i] == dominoes[j]:
                res += dominoes[i] * middle
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                res += '.' * middle
            else:
                res += 'R' * (middle / 2) + '.' * (middle % 2) + 'L' * (middle / 2)
            i = j
        return res