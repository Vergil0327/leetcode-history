# Intuition

根據example 2, 我們知道我們可以任意互換, 也就是可以任意重新放置字母去形成palindrome
全部words[i]可以視為一個字典, 要盡可能利用每個字母形成長度為len(words[i])的palindrome
那長度小的肯定比長度大的還容易組成, 首先想到的是盡可能地以greedy的方式去優先組成較短的palindrome
由短到長去利用可用letter組成palindrome

因此我們先找出我們有多少個pair以及能作為palindrome中心的字母
```py
count = Counter()
for word in words:
    for ch in word:
        count[ch] += 1

pairs = mid = 0
for cnt in count.values():
    pairs += cnt//2
    mid += cnt%2
```

再來就從短到長, 看我們能組出多少合法palindrome
```py
sizes = [len(word) for word in words]
sizes.sort()
```

我們盡可能把可分配的pair分配下去
```py
for i in range(n):
    need_pair = sizes[i]//2
    if pairs >= need_pair:
        pairs -= need_pair
        sizes[i] -= need_pair*2
    else:
        break
```
然後再看我們有多少合法palindrome, 如果是奇數長度palindrome, 我們就看我們還有沒有可分配字母

```py
for i in range(n):
    need_pair = sizes[i]//2
    if pairs >= need_pair:
        pairs -= need_pair
        sizes[i] -= need_pair*2
    else:
        break

mid += pairs * 2
res = 0
for i in range(n):
    if sizes[i] == 0:
        res += 1
    elif sizes[i] == 1 and mid > 0:
        mid -= 1
        res += 1
    else:
        break
return res
```