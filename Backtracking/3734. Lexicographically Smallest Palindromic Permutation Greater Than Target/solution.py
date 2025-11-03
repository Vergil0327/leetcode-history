class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:        
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        mid = ''
        for i in range(26):
            if count[i] % 2 != 0:
                if not mid:
                    mid = chr(i + ord('a'))
                else:
                    return "" # multiple middle character => invalid

        half_cnt = [x // 2 for x in count]
        n = len(s) // 2
        pal = [''] * n

        def dfs(i, is_greater):
            if i >= n:
                rev = pal[::-1]
                res = ''.join(pal) + mid + ''.join(rev)
                return res > target

            start = 'a' if is_greater else target[i]
            for c_ord in range(ord(start), ord('z') + 1):
                c = chr(c_ord)
                if half_cnt[c_ord - ord('a')] > 0:
                    pal[i] = c
                    half_cnt[c_ord - ord('a')] -= 1
                    if dfs(i + 1, is_greater or c > target[i]):
                        return True
                    half_cnt[c_ord - ord('a')] += 1
            return False

        if dfs(0, False):
            rev = pal[::-1]
            return ''.join(pal) + mid + ''.join(rev)
        return ""