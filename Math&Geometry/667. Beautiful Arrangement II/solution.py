class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        l, r = 1, n
        res = []
        rounds = 1
        while l <= r:
            if k > 1: # append interleavely to get distinct difference from n-1, n-2, n-3, ...
                if rounds%2 == 0:
                    res.append(l)
                    l += 1
                else:
                    res.append(r)
                    r -= 1
                rounds += 1
            else: # just append the remaining numbers in order to make all the difference are 1
                if rounds%2 == 0:
                    res.append(l)
                    l += 1
                else:
                    res.append(r)
                    r -= 1

            k -= 1
        return res
