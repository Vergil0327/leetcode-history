class Solution:
    def minFlips(self, target: str) -> int:
        groups = [g for g in groupby(target)]
        
        flip = 0
        for i in range(len(groups)):
            if flip%2 + int(groups[i][0]) == 0: continue
            flip += 1
        return flip

class Solution:
    def minFlips(self, target: str) -> int:
        flip = 0
        last = "0"
        for i in range(len(target)):
            if target[i] != last:
                last = target[i]
                flip += 1
        return flip

