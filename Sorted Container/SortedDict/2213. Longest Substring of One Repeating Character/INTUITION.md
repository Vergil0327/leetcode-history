# Intuition

think brute force first O(k*n)

```py
n = len(s)
arr = list(s)
res = []
for i, ch in zip(queryIndices, queryCharacters):
    arr[i] = ch

    ans = length = 0
    prev = ""
    for j in range(n):
        if arr[j] == prev:
            length += 1
        else:
            length = 1
            prev = arr[j]
        ans = max(ans, length)
    res.append(ans)
return res
```

但對於substring長度, 要怎樣才能動態更新又要能找出高效找出最長substring長度?
如果我們找出該字母的所有substring區間[[l1, r1], [l2, r2], ...]並且為有序的
就能用binary search找出`idx = updates[ch][j]`在該字母的區間位置, 以及相鄰左右兩區間

假如s[i]有更動, 亦即`s[i]!=queryCharacter`
那麼插入前檢查需不需要break interval
插入後看需不需要merge interval, 然後更新長度
如此一來, 這就是個維護有序區間的問題了

由於要能高效更新interval, 所以可能sorted dict比較適合
同時為了方便快速更新當前最長length, 在用sorted list來維護substring length

SortedDict: interval[start_index]: substring length
SortedList: substrLength = [len1, len2, ...]

```py
interval = SortedDict()
curIdx = -1
for i in range(n):
    if i == 0 or s[i] != s[i-1]:
        interval[i] = 1
        curIdx = interval.index(i)
    else:
        k, v = interval.peekitem(curIdx)
        interval[k] += 1

substrLength = SortedList()
for length in interval.values():
    substrLength.add(length)
```

再來就開始判斷每個query會不會:
1. break existing interval
   - 如果size=1, 那替換後size不變
   - size > 1, 那就看query_character的位置是在兩端還是在中間來break interval
     - 並同步更新`interval`, `length`

```py
if ch != arr[i]:
    arr[i] = ch

    idx = interval.bisect_right(i)-1
    
    # break interval
    j, size = interval.peekitem(idx)
    # j______i
    # i j_____
    # j__ i j_
    if size > 1:
        del interval[j]
        length.remove(size)

        if i == j: # i為左端點
            interval[i] = 1
            length.add(1)

            interval[j+1] = size-1
            length.add(size-1)
            
        elif i == j+size-1: # i為右端點
            interval[i] = 1
            length.add(1)

            interval[j] = size-1
            length.add(size-1)
        else: # # i在中間, 會形成三個interval
            interval[i] = 1
            length.add(1)
            
            interval[j] = i-j
            length.add(interval[j])

            interval[i+1] = size - (i-j+1)
            length.add(interval[i+1])
```

2. merge interval
    - break完後, 就判斷能不能merge
    - 如果s[i] == s[i+1] => merge right interval
    - s[i] == s[i-1] => merge left interval

```py
## check merge right
if i+1<n and ch == arr[i+1]:
    idx = interval.bisect_right(i)
    j, size = interval.peekitem(idx)
    length.remove(size)
    length.remove(interval[i])
    del interval[j]

    interval[i] = interval[i]+size
    length.add(interval[i])

## check merge left
if i-1 >= 0 and ch == arr[i-1]:
    l = interval.bisect_left(i)-1
    j, size = interval.peekitem(l)
    length.remove(interval[i])
    length.remove(size)
    interval[j] = size+interval[i]
    length.add(interval[j])
    del interval[i]
```

整體時間複雜度就$O(klogn)$