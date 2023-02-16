# Intuition

這題要求的是我們要分別找出leftmost index跟rightmost index
我們把`t[leftmost:rightmost]`全部刪除後剩下的`t`為`s`的subsequence
這時的分數 `score` 為刪除的個數 `rightmost-rightmost+1`
我們要求的是最少分數是多少

*求最少分數，要麻DP、要麻binary search、要麻Greedy*

這題的最佳解為Greedy

首先如果要讓分數最少，代表[leftmost, rightmost]這區間要最小
也就是prefix t[:leftmost], suffix t[rightmost:]要最長並且 t[:leftmost] + t[rightmost+1:] 為subsequence of s

首先我們先遍歷一遍找出每個位置的leftmost[i]

```py
M, N = len(s), len(t)
leftmost = []
j = 0
for i in range(M):
    if j < N and s[i] == t[j]:
        j += 1
    leftmost.append(j)
```

這時最後的`j`，代表t[:j]為subsequence of s
score 至少為 `N-j` (刪掉t[j:]只留下t[:j])

再來我們反過來看rightmost:
在`i`位置時，的leftmost[i]已經確定，我們可以盡可能的找出最長的合法suffix subsequence並更新score:

`score = min(score, max(rightmost-leftmost[i]+1, 0))`,
其中 `max(rightmost-leftmost[i]+1, 0)` 是因為 left 必須小於等於 right (deletion必須大於等於0)

只要s[i] == t[rightmost]，代表在i位置上找到一個character是subsequence of s一部分
我們可以移動rightmost deletion的index位置
```
if rightmost >= 0 and s[i] == t[rightmost]:
    rightmost -= 1
```

```py
rightmost = N-1
for i in range(M-1, -1, -1):
    # rightmost index must >= leftmost index
    # deletion can't be negative
    score = min(score, max(rightmost-leftmost[i]+1, 0))

    if rightmost >= 0 and s[i] == t[rightmost]:
        rightmost -= 1

return min(score, rightmost-0+1)
```

最後記得在跟把`t[:rightmost]`全刪掉的分數做比較，這時left index為0
因此把t[:rightmost]全刪掉的分數為 `rightmost-0+1`
