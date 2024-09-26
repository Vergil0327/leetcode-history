class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        arr0, arr1 = [], []
        for i in range(n):
            if s[i] == "0":
                arr0.append(i)
            else:
                arr1.append(i)
        if abs(len(arr0) - len(arr1)) > 1: return -1

        if len(arr0) > len(arr1):
            diff = 0
            for i in range(n):
                if i%2 == 0:
                    diff += int(s[i] == "1")
                else:
                    diff += int(s[i] == "0")
            return diff//2
        elif len(arr0) < len(arr1):
            diff = 0
            for i in range(n):
                if i%2 == 0:
                    diff += int(s[i] == "0")
                else:
                    diff += int(s[i] == "1")
            return diff//2
        else: # len(arr0) == len(arr1):
            diff1 = 0
            for i in range(n):
                if i%2 == 0:
                    diff1 += int(s[i] == "1")
                else:
                    diff1 += int(s[i] == "0")

            diff2 = 0
            for i in range(n):
                if i%2 == 0:
                    diff2 += int(s[i] == "0")
                else:
                    diff2 += int(s[i] == "1")
            return min(diff1, diff2)//2
