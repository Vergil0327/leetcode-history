# Intuition

if we cut more, sweetness will be smaller if total cuts are valid
if we cut less, sweetness will be greater if total cuts are valid

thus, we can use binary search to guess sweetness.

search space we can roughly define `[min(sweetness), sum(sweetness)]` from eat just one piece to eat them all.

and we can greedily check if our guess is valid or not.

greedily cut as much as possible if sweetness is greater than or equal to our guess.

```py
def check(guess):
    cnt = 0
    curr = 0
    for sweet in sweetness:
        curr += sweet
        if curr >= guess:
            curr = 0
            cnt += 1
    return cnt >= (K+1)
```

then, the binary search pattern is easy:
if guess of this time is valid, it can be possible answer and we can upper our lowerbound to `mid`, else lower our upperbound to `mid-1`

```py
l, r = min(sweetness), sum(sweetness)
while l < r:
    mid = r - (r-l)//2
    if check(mid):
        l = mid
    else:
        r = mid-1
return l
```

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(1)$$