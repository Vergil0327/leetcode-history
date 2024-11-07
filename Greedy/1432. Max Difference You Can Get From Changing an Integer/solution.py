class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        n = len(s)

        mx = s
        for i in range(n):
            if s[i] != "9":
                mx = mx.replace(s[i], "9")
                break
        mx = int(mx)

        pick = -1
        arr = list(s)
        if s[0] > "1":
            for i in range(n):
                if arr[i] == s[0]:
                    arr[i] = "1"
        else:
            for i in range(1, n):
                if s[i] == "0": continue
                if s[i] == s[0]: continue
                pick = i
                break

            if pick > -1:
                for i in range(1, n):
                    if arr[i] == s[pick]:
                        arr[i] = "0"
        mn = int("".join(arr))

        return mx-mn
