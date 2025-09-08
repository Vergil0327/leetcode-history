class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        if n == 0: return 1 # avoid negative shift

        L = n.bit_length()

        res = 1 # "0"
        for i in range(1, L):
            half = (i+1)//2
            mn, mx = 1<<(half-1), (1<<half)-1
            res += mx-mn+1

        def build(half: int, L: int):
            bits = bin(half)[2:]
            while len(bits) < (L+1)//2:
                bits += "0"

            if L%2 == 0:
                return int(bits + bits[::-1], 2)
            else:
                return int(bits + bits[:-1][::-1], 2)

        half = (L+1)//2
        mn, mx = 1<<(half-1), (1<<half)-1
        l, r = mn, mx
        while l < r:
            mid = r - (r-l)//2
            palindrome = build(mid, L)
            if palindrome <= n:
                l = mid
            else:
                r = mid-1
        
        palindrome = build(l, L)
        if palindrome <= n:
            res += l - mn + 1
        return res
        