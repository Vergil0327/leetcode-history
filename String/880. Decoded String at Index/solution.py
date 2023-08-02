class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                times = int(ch)
                if n * times < k:
                    n *= times
                else:
                    if k%n == 0: # n-th character
                        return self.decodeAtIndex(s[:i], n)
                    else: # k%n -th character
                        return self.decodeAtIndex(s[:i], k%n)
            else:
                n += 1
                if n == k:
                    return ch
        return ""
    

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                n *= int(ch)
            else:
                n += 1
            if n >= k: break

        for j in range(i, -1, -1):
            if s[j].isdigit():
                n /= int(s[j])
                k %= n
            else:
                if k == n or k == 0: return s[j]
                n -= 1
        return ""