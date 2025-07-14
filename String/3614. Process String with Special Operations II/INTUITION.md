
# Intuition

操作:
- If the letter is a lowercase English letter append it to result.
- A '*' removes the last character from result, if it exists.
- A '#' duplicates the current result and appends it to itself.
- A '%' reverses the current result.

首先我們可以先確認有沒有解:

```py
n = len(s)

size = 0
for i in range(n):
    if s[i].isalpha():
        size += 1
    elif s[i] == '*' and size > 0:
        size -= 1
    elif s[i] == '#':
        size *= 2
if k >= size: return "."
```

再來想法是我們逆推回來, 從k-th character, 逆向操作反推回原本的s[i]
從上述確認我們可以順便求得最終長度`size`, 逆推回來直到`size == k`的當下, 代表我們當前這個操作加上s[i]時, 會是剛好final_string[k]

```py
for i in range(len(s) - 1, -1, -1):
    if s[i] == '*':
        size += 1
    elif s[i] == '#':
        size //= 2
        if k >= size:
            k -= size
    elif s[i] == '%':
        k = size - 1 - k
    else:
        size -= 1
        if size == k: # found it
            return s[i]
return "."
```