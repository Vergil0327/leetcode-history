class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        n = len(s)
        if all(target[i] == "0" for i in range(n)):
            return all(s[i] == "0" for i in range(n))
        if all(s[i] == "0" for i in range(n)):
            return all(target[i] == "0" for i in range(n))
        return True
