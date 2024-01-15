class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def check(num, k, x):
            bits = list(map(int, bin(num)[2:][::-1])) # bits = [低位, ..., 高位]

            tot = 0
            i = x-1 # 1-indexed to 0-indexed
            while (1<<i) <= num:
                if bits[i] == 0:
                    XXX = 0
                    for j in range(len(bits)-1, i, -1):
                        XXX = XXX*2 + bits[j]
                    tot += XXX * pow(2, i)
                else:
                    XXX = 0
                    for j in range(len(bits)-1, i, -1):
                        XXX = XXX*2 + bits[j]
                    tot += XXX * pow(2, i)

                    YYY = 0
                    for j in range(i-1, -1, -1):
                        YYY = YYY*2 + bits[j]
                    tot += YYY+1
                i += x
            return tot <= k
        l, r = 1, 10**15
        while l < r:
            mid = r - (r-l)//2
            if check(mid, k, x):
                l = mid
            else:
                r = mid-1
        return l
