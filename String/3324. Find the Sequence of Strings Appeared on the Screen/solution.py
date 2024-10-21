class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []

        while target:
            preifx = target[:-1]
            last = ord(target[-1])-ord("a")
            while last >= 0:
                res.append(preifx+chr(last+ord("a")))
                last -= 1
            target = preifx
        res.reverse()
        return res
