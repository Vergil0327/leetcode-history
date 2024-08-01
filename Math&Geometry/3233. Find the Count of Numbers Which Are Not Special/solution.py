class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        ll, rr = ceil(sqrt(l)), floor(sqrt(r))
        special = 0
        for i in range(max(2, ll), rr+1):
            valid = True
            for j in range(2, int(sqrt(i))+1):
                if i%j == 0:
                    valid = False
                    break

            special += int(valid)
        return r-l+1 - special
