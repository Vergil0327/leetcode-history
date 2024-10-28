# Intuition

z -> ab -> z(ab) -> (ab)bc -> z(ab)

狀態轉移很明顯:
1. "a"從"z"轉移過來
2. "b"從"a"跟"z"轉移過來
3. 其餘"c", "d", ..., "z"從前個字母轉移過來

所以我們就定義length[i] = the length of i-th character at current rounds
然後再遍歷`t`次, 更新每個字母的長度狀態即可

time: O(n + 26t)
space: O(26)