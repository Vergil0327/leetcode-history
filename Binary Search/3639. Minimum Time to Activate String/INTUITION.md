# Intuition

t越大, `*`越多 => 單調遞增
所以首先想到用binary search說猜這個t, 然後以greedy的方式確認當前`s`是否合法

主框架:
```py
l, r = 0, len(order)
while l < r:
    mid = l + (r-l)//2
    x = count(mid)

    if x < k:
        l = mid+1
    else:
        r = mid
return l if l < len(order) else -1
```

所以現在欠缺的就是如何計算有多少的含有至少一個`*`的合法subarray

```
total subarray = len(s) * (len(s)+1) // 2
valid = total - invalid
```

invalid比較好算, 我們只需要找出被`*`間隔出來的所有不含`*`的subarray
去計算他們貢獻的subarray數目即可

helper function:

```py
n = len(s)
total_subarr = n * (n+1) // 2
def count(t):
    position = []
    for i in range(t+1):
        position.append(order[i])
    position.sort()
    m = len(position)
    
    left_invalid = 0 if not position else (position[0] * (position[0]+1) // 2)
    right_invalid = 0 if not position else ((n-1-position[-1]) * (n-1-position[-1]+1) // 2)
    mid_invalid = 0
    for i in range(1, m):
        length = position[i]-position[i-1]-1
        mid_invalid += length * (length+1) // 2
    return total_subarr - mid_invalid - left_invalid - right_invalid
```