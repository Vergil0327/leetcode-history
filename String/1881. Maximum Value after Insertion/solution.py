class Solution:
    def maxValue(self, n: str, x: int) -> str:
        positive = n[0] != "-"
        s = n if positive else n[1:]

        if positive:
            i = 0
            while i < len(s) and x <= int(s[i]):
                i += 1
            return s[:i] + str(x) + s[i:]

        else:
            i = 0
            while i < len(s) and x >= int(s[i]):
                i += 1
            return "-" + s[:i] + str(x) + s[i:]