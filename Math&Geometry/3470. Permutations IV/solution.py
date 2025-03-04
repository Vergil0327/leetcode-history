class Solution:
    def permute(self, N, K):
        res = []
        vals = list(range(1, N + 1))
        parity = 1

        # find digit in i-th position
        for i in range(N):
            # If n - i numbers are left, the count of permutations is:
            # fact((n - i) / 2) × fact((n - i - 1) / 2)
            perms = factorial((N - 1 - i)//2) * factorial((N - i)//2)

            # iterate candidates and find first value which its permutations is greater than need
            # then add it to result and remove it from candidates
            # keep finding next value
            for j, v in enumerate(vals):
                if v % 2 != parity and (i or N % 2):
                    continue
                if K <= perms:
                    break
                K -= perms
            else:
                return []

            res.append(vals.pop(j))
            parity = res[-1] & 1 ^ 1

        return res
