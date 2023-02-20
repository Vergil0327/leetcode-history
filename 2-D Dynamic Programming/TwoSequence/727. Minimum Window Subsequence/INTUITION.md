# Intuition

想法是用sliding window的概念去找有沒有包含t這個subsequence

我們持續移動`r` pointer，並用`i`紀錄我們目前的window包含了t[:i]

等到 i == len(t) 代表目前的window存在著subsequcne為t
這時我們從`r`邊界開始回頭找，找出最短window並包含t的window

回頭找時每當s[j] == t[i]，i-= 1，直到i < 0

由於每當找到一個可行解後，重置i=0，並且由於`r`會持續往右走
所以每個字符最多就遍歷兩次，因此時間複雜度為O(n)