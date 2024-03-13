# Intuition

s = XXXXXXXXX
subseq = []

brute force: subseq => take or skip, but Memory limit exceeded

```py
n = len(s)
@cache
def dfs(i, size, rep):
    if size == k:
        return "" if rep <= 0 else "*"
    if i == n: return "*"
    
    x = dfs(i+1, size, rep)
    y = s[i] + dfs(i+1, size+1, rep-int(s[i] == letter))
    if x.endswith("*"):
        return y
    elif y.endswith("*"):
        return x
    else:
        return min(x, y)
return dfs(0, 0, repetition)
```

由於跟substring有關, 想看看有沒有greedy solution
首先想到的是利用stack維護subseq, 再看看怎麼維護

lexicographically smallest => 整個subseq.必須是monotonically increasing sequence
總共有`k`個字符, 其中必須有`repetition`個letter
代表其餘字符僅能有`k-repetition`個

且所以對於整個長度為`n`的`s`來說:
- 最多pop掉n-k次
- 並且其中最多pop掉`Counter(s)[letter]-repetition`個letter

所以在滿足以上兩個情況下, 我們能盡可能地利用monotonically increasing stack來構造subseq
我們分別用`deleted`, `letterDeleted`兩個變數來分別維護上面兩種情形

1. `deleted` at most `n-k`
2. `letterDeleted` at most `numLetters - repetition`

這樣的話, 在構造過程中只要`deleted`跟`letterDeleted`仍滿足條件
我們遇到stack[-1] > s[i]的時候, 就能盡可能地去刪除stack[-1]來構造lexicographically increasing subseq:


```py
n = len(s)

numLetters = sum(1 for ch in s if ch == letter)
upperbound1, upperbound2 = n-k, numLetters-repetition
deleted = letterDeleted = 0

stack = []
for i in range(n):
    while (stack and stack[-1] > s[i]
                    and deleted < upperbound1
                    and (letterDeleted < upperbound2 if stack[-1] == letter else True)):
        deleted += 1
        letterDeleted += int(stack.pop() == letter)
    
    stack.append(s[i])
```

那這樣最後stack存的就是符合條件的lexicographically increasing subseq.
但我們最終要的是恰好長度為`k`且letter至少有`repetition`個的subseq.
因此我們從後往前掃一遍, 看還有哪些可以刪除, 直到最終長度為`k`且letter至少有`repetition`

```py
res = ""
for i in range(len(stack)-1, -1, -1):
    if deleted == upperbound1: # can't delete anymore
        res = stack[i] + res
    elif stack[i] == letter and letterDeleted == upperbound2: # can't delete letter anymore
        res = stack[i] + res
    else:
        deleted += 1
        letterDeleted += int(stack[i] == letter)
return res
```