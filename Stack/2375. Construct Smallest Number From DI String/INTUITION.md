# Intuition

III: increasing subseq.
DDD: decreasing subseq.

所以我們greedily從num=1開始:
1. 連續遇到"D", 先將num存放到stack2, 後續等到"I"的時候在逆序放置回去
2. 連續遇到"I", 直接將num存放到stack1形成increasing subseq., 並且如果之前有任何存放在stack2的數, 再逆序pop回來滿足先前存放的"DDD..." decreasing subseq.