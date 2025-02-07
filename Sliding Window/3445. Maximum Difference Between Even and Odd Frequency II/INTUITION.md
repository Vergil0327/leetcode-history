# Intuition

### brute force solution

```py
n = len(s)

def diff(i, j):
    count = Counter(s[i:j+1])
    odd, even = -inf, inf
    for v in count.values():
        if v % 2 == 0:
            even = min(even, v)
        else:
            odd = max(odd, v)
    return odd-even

res = -inf
for length in range(k, n+1):
    for i in range(n-length+1):# j = i+length-1 < n
        j = i+length-1
        res = max(res, diff(i, j))
return res
```

我們需要一個更高效查找的方式

限制上注意到: s consists only of digits '0' to '4'.
odd-even組合最多就這20種可能:
    - 奇數個 0 搭配偶數個 1,2,3,4
    - 奇數個 1 搭配偶數個 0,2,3,4
    - 奇數個 2 搭配偶數個 0,1,3,4
    - 奇數個 3 搭配偶數個 0,1,2,4
    - 奇數個 4 搭配偶數個 0,1,2,3

這數據規模看起來感覺我們可以針對這些組合去找出max difference
```py
for odd in "01234": 
    for even in "01234": 
        if odd == even: continue

        # find maximum difference here
```

那針對尋找substring最大even或最小odd, 首先想到prefix sum + hashmap

```
s = X X X {X X X X X X X X X X}
           l                 r
```

對於當前s[r]來說, 假設我們現在要找s[r]的odd frequency
那麼我們可以用presum[r] - seen_presum[l]來計算, 其中:
- 如果presum[r]是偶數, 那麼就要找一個是奇數的seen_presum[l]
- 如果presum[r]是奇數, 那就要找一個偶數的seen_presum[l]
那麼s[l:r]這段區間裡, s[r]就會odd frequency

同理, 我們再找一個s[r']是最小even frequency
那麼一樣可以利用presum[r'] - seen_presum[l']來計算, 其中:
- 如果presum[r']是偶數, 那麼要找一個同樣是偶數的seen_presum[l']
- 如果presum[r']是奇數, 那麼要找一個同樣是奇數的seen_presum[l']
那麼s[l:r]這段區間裡, s[r]就會even frequency

那綜合以上, 我們現在要找的是max difference of (odd frequency - even frequency)

所以就是(presum[r]-presum[l]) - (presum[r']-presum[l'])要最大, 其中:
- presum[r]-presum[l]必須是奇數
- presum[r']-presum[l']必須是偶數

轉換一下變成: (presum[r]-presum[r']) - (presum[l]-presum[l'])要最大, 那代表:
- presum[r]-presum[r']要盡可能大
- presum[l]-presum[l']要盡可能小

那綜合上述, 我們利用sliding window

首先我們持續移動右指針, 紀錄presum_odd跟presum_even

```py
while r < n:
    presum_odd.append(presum_odd[-1])
    presum_even.append(presum_even[-1])
    
    # expands the window by adding new characters and updating their frequencies.
    ch = s[r]
    if ch == odd:
        presum_odd[-1] += 1
    elif ch == even:
        presum_even[-1] += 1
    r += 1
```

再來考慮window size constraint, 這是最重要的一步:

```
s = X X X X X X X X X X X X X {X X X X}
    l ->                       l     r
```

這邊我們限制`while r-l >= k and presum_odd[l] < presum_odd[-1] and presum_even[l] < presum_even[-1]`就往右移動l
這目的是去計算對於當前`r`位置的presum_odd[r]-presum_even[r]來說, 所有所需的合法奇偶性互補presum_odd[l]-presum_even[l] (previous valid prefix sum with complementary parities)
> 這段while-loop 限制`r-l >= k`所記錄到`seen`裡的presum diff, 與我們當前的diff相減, size必定至少為k

然後這邊我們再以(presum_odd[l], presum_even[l])的奇偶性作為key, 持續紀錄minimum difference with wanted parity (odd, even)

```py
# Window Size Constraint
# seen[key]: minimum previous frequencies with complementary parities
while r-l >= k and presum_odd[l] < presum_odd[-1] and presum_even[l] < presum_even[-1]:
    key = (presum_odd[l] % 2, presum_even[l] % 2) # parity of odd & even
    diff = presum_odd[l] - presum_even[l]
    seen[key] = min(seen[key], diff)
    l += 1
```

那等到這上面這段跑完, 對於當前presum_odd[r]-presum_even[r]來說, 所有奇偶性的最小presum_odd[l]-presum_even[l]都有了
並且size constraint也符合至少為`k-size`, 所以我們從`seen`中找出所需即可

當前prefix sum為: `current = presum_odd[-1] - presum_even[-1]`
那我們再根據當前的presum_odd[-1]跟presum_even[-1]的奇偶性找出我們所需的互補prefix sum

wanted_key = (1 - presum_odd[-1] % 2, presum_even[-1] % 2) # wanted parity of odd & even
那麼: `current - seen[wanted_key]` 就能得到maximum difference considering s[:r]