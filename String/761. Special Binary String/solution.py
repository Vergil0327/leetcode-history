class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        i = 0
        n = len(s)

        strs = []
        while i < n:
            i0 = i
            count = 0

            while i < n:
                if s[i] == "1":
                    count += 1
                else:
                    count -= 1
                if count == 0: break
                i += 1

            middle = self.makeLargestSpecial(s[i0+1:i])
            strs.append("1" + middle + "0")
            i += 1

        strs.sort(reverse=True)
        return "".join(strs)
