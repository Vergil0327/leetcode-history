# Intuition

所謂的good array, 必須滿足 i <= k <= j
所以我們把整個nums從k位置分成兩半來看:
```
X X X X X X  [X]   X X
              k
              l
              r
```

由於我們要找的是subarray, 所以我們可以用two pointers `l` and `r` 來代表subarray的左右邊界
再來就是看如果加上左邊的nums[l-1]後score比加上nums[r+1]後的score還要高，那就把左邊界往右移
反之，就把右邊界往右移

透過 `min([nums[l:r]) * subarray_size` 這個公式來移動左右邊界

由於我們每加入一個數後，都要知道當下subarray的最小值，所以我們另外用min heap來幫我麼快速找出min(nums[l:r])

```
X X X X [X X X X X] X X X X
      <- l   k   r ->
minHeap = [X X X X X X X]
```

因此我們在two pointers`l`跟`r`都不越界的情況下由內往外

```py
while l >= 0 and r < n:
    if l-1 >= 0 and r+1<n:
        left = min(window[0][0], nums[l-1])
        right = min(window[0][0], nums[r+1])
        if left > right:
            l -= 1
            heapq.heappush(window, [nums[l], l])
        else:
            r += 1
            heapq.heappush(window, [nums[r], r])
    elif l-1 >= 0:
        l -= 1
        heapq.heappush(window, [nums[l], l])
    elif r+1 < n:
        r += 1
        heapq.heappush(window, [nums[r], r])
    else:
        break
    res = max(res, window[0][0]*(r-l+1))
```

等到上面的while-loop跳出來後
有可能`l >= 0`仍成立，抑或是`r < n`仍成立

所以我們繼續遍歷剩餘可能性:
```py
while l-1 >= 0:
    l -= 1
    heapq.heappush(window, [nums[l-1], l])
    res = max(res, window[0][0]*(r-l))
while r+1 < n:
    r += 1
    heapq.heappush(window, [nums[r+1], r])
    res = max(res, window[0][0]*(r-l))
```

最終答案就是`res`

# Optimized

的仔細想想，由於是good array在移動左右邊界時
加入後的nums[i]會一直在裡面，所以其實不需要min heap
只需要在移動左右邊界時，持續更新min value即可

```py
# 移動左邊界時更新minVal
minVal = min(minVal, nums[l])

# 移動右邊界時更新minVal
minVal = min(minVal, nums[r])
```

# Concise

最後我們可以把程式碼整理一下, 由於最後目標是把整個`nums`遍歷完
所以我們可以把三個while-loop merge在一起，把條件改成`while l > 0 or r < n-1`
確保score公式中的`r-l+1`成立

```py
n = len(nums)
l = r = k
res = minVal = nums[k]
while l > 0 or r < n-1:
    # logic here..
    
return res
```

那while-loop裡面的邏輯跟前面一樣
- 如果nums[l-1] > nums[r+1], 那就移動左邊界 `l -= 1`
  - 一但左邊界走到底，那就把值設為`-inf`, 這樣就肯定會選擇移動右邊界
- 反之, 就移動右邊界`r += 1`
  - 一但右邊界走到底，同樣就把值設為`-inf`, 這樣就肯定會移動左邊界

```py
while l > 0 or r < n-1:
    left = nums[l-1] if l-1 >= 0 else -inf
    right  = nums[r+1] if r+1 < n else -inf
    if left > right:
        minVal = min(minVal, left)
        l -= 1
    else:
        minVal = min(minVal, right)
        r += 1
    res = max(res, minVal * (r-l+1))
```

最終程式碼就可整理為僅僅20行左右