
class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        size = 0
        for i in range(n):
            if s[i].isalpha():
                size += 1
            elif s[i] == '*' and size > 0:
                size -= 1
            elif s[i] == '#':
                size *= 2
        if k >= size: return "."

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '*':
                size += 1
            elif s[i] == '#':
                size //= 2
                if k >= size:
                    k -= size
            elif s[i] == '%':
                k = size - 1 - k
            else:
                size -= 1
                if size == k: # found it
                    return s[i]
        return "."