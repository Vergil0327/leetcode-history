# Intuition

直覺想到的是我們肯定是優先用次數最多的字母來組
然後每當遇到限制, 便改拿次大的字母
持續到沒有辦法構造為止

由於我們要持續找出剩餘次數最多的字母, 所以我們可以用**max heap**來儲存`[remain_count, character]`
然後再判斷當前是不是可以合法構造的狀況即可:
- if len(s) > 1 and s[-1] == ch and s[-2] == ch: use 2nd largest remain_count character
- else: use current character directly