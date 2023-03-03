# Intuition

由於 `ord(a) < ord(e) < ord(i) < ord(o) < ord(u)`

所以我們遍歷一遍，只要 word[i] >= word[i-1] 那就可以append上去形成 possible beautiful substring

- 每當 word[i] > word[i-1] 代表我們找到一個新的vowel，當我們湊齊5個vowel就可以更新我們的答案

- 當word[i] > word[i-1]，就繼續延長長度

word[i] < word[i-1]，代表我們只能從這點開始，重新找beautiful substring