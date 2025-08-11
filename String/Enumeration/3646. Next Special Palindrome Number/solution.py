from itertools import permutations


class Solution:
    def specialPalindrome(self, n: int) -> int:
        odd = ['', '1', '3', '5', '7', '9']
        even = ['2', '4', '6', '8']
        states = 1<<len(even)

        res = float('inf')
        for mid in odd:
            digits = []
            if mid and int(mid) > 1:
                for _ in range(int(mid)//2):
                    digits.append(mid)

            for state in range(states):
                left = digits.copy()
                for i in range(len(even)):
                    if (state>>i)&1:
                        left += [even[i]] * (int(even[i])//2)
                if not mid and not left: continue

                length = len(left)*2 + (0 if not mid else 1)
                if length < len(str(n)): continue
                if length > len(str(n)) + 1: continue
                
                for perm in permutations(left, len(left)):
                    s = "".join(perm)
                    candidate = int(s + mid + s[::-1])
                    if candidate > n:
                        res = min(res, candidate)
        return res