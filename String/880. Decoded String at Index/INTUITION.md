# Intuition

如果當前decoded string長度是n, 那長度的增長如下
```py
n = 0
for i, ch in enumerate(s):
    if ch.isdigit():
        times = int(ch)
        n *= times
    else:
        n += 1
```

我們目標是找出`n == k`這個位置的character, 所以:
- 在ch.isalpa()時, 如果n==k直接返回ch
- 如果n * times剛好等於k時, 代表k-th character是這個循環string的最後一位, 也就是第n位字符. 相當於在s[:i]這裡面找第n個character, 所以是`decodeAtIndex(s[:i], n)`
- 如果n * times大於k時, 代表k-th character是循環string的第`k%times -th` character, 也就是`decodeAtIndex(s[:i], k%n)`

綜上所述, 這剛好是個遞歸(divide and conquer)

# Other Solution

也可以用iterative的方式

首先先找出循環string.size >= k的時候的位置
然後再從該位置由後往前倒推回來

- 如果s[i]是digit, `k %= n`
- 如果s[i]是alpha, `k -= 1`
- 當k == n or k == 0時, 都代表當前ch是循環string中我們要的該位character