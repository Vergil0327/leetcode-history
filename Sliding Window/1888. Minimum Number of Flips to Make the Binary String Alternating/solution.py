class Solution:
    def minFlips(self, s: str) -> int:
        alt0 = alt1 = ""
        diff0 = diff1 = 0
        for i, ch in enumerate(s):
            if i%2 == 0:
                alt0 += "0"
                alt1 += "1"
                if ch == "0":
                    diff1 += 1
                else:
                    diff0 += 1
            else:
                alt0 += "1"
                alt1 += "0"
                if ch == "0":
                    diff0 += 1
                else:
                    diff1 += 1

        # 010 => 010101
        # 101 => 101010
        # 0101 => 01010101
        # 1010 => 10101010
        n = len(s)
        alt0 = alt0+alt0 if n%2 == 0 else alt0+alt1
        alt1 = alt1+alt1 if n%2 == 0 else alt1+alt0

        res = min(diff0, diff1)
        rotate = deque(s)
        for i in range(n):
            ch = rotate.popleft()
            
            if ch == alt0[i]:
                diff0 += 1
            if ch == alt1[i]:
                diff1 += 1

            if ch == alt0[i+n]:
                diff0 -= 1
            if ch == alt1[i+n]:
                diff1 -= 1

            rotate.append(ch)
            res = min(res, min(diff0, diff1))
        return res