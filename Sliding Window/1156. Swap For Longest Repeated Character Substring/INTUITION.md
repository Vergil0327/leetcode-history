# Intuition

首先想到的是:

最多26個英文字並且最多swap一次
因此我們能先遍歷當前要找的最長repeated character substring (a-z), 然後以O(n)時間進行slinding window
sliding window過程中允許一個不同的字母進行交換(如果window外仍有字母可交換的話)
持續透過sliding window找出最長substring length

time: O(26n)
space: O(26)

# Intuition 2 (Optimized)

仔細想一下, 如果我們能swap一次, 那麼該repeated substring必定是由**2個**repeated substring 以及任意一個字母組成


```
OOOOOOOOOOOOOOOOOOOOOOOOOOO X OOOOOOOOOOOOOO
 left repeated substring       right repeated substring 
```

那麼我們只需要用two pointers來找出該情況即可:

```py
count = Counter(text)

i, n = 0, len(text)
res = 1
while i < n:
    # left: left repeated substr length
    # right: right repeated substr length
    left = right = 0

    while (i + left < n) and (text[i] == text[i + left]):
        left += 1

    start = i + left + 1
    while (start + right < n) and (text[i] == text[start + right]):
        right += 1

    res = max(res, min(count[text[i]], left + right + 1))
    i += left

return res
```

time: O(n)
space: O(26)