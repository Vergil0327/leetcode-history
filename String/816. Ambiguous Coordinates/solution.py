class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        n = len(s)

        res = set()
        for i in range(1, n):
            left, right = s[:i], s[i:]

            valsL = self.make_num(left)
            valsR = self.make_num(right)
            for j in range(len(valsL)):
                for k in range(len(valsR)):
                    res.add(f"({valsL[j]}, {valsR[k]})")

            # one-line
            # for v1, v2 in itertools.product(valsL, valsR):
            #     res.add(f"({v1}, {v2})")
            
        return list(res)

    def make_num(self, num):
        nums = []
        for j in range(len(num)):
            integer, fraction = num[:j+1], num[j+1:]
            if len(integer) > 1 and integer[0] == "0": continue # leading zero
            if fraction.count("0") == len(fraction): continue # .0000 (X)
            if fraction.endswith("0"): continue # 2.30 (X)
            nums.append(integer + ("." + fraction if fraction else ""))
        
        if not (len(num) > 1 and num[0] == "0"): # leading zero
            nums.append(num)
        return nums
