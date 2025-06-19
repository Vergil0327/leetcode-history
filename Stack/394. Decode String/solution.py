class Solution:
    def decodeString(self, s: str) -> str:
        count = 0
        stack = []
        cur = ''
        for ch in s:
            if ch.isdigit():
                count = count * 10 + int(ch)
            elif ch == '[':
                stack.append((cur, count))
                cur = ''
                count = 0
            elif ch == ']':
                prefix, times = stack.pop()
                cur = prefix + cur * times
            else:
                cur += ch
        return cur