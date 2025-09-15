# Intuition

problem doesn't articulate well.

simplified to say, we simulate the process and keep tracking the number of element in slidinw window and which element is discarded or not in sliding window.

```py
# should make sure sliding window is not greater than `w`
if count[num] < m:
    count[num] += 1
else:
    discardElem.add(r)
    discard += 1
```

when we shrink our sliding window when width is over `w`, we only decrease the number in hashmap when this element is **NOT** discarded

```py
while l < r and r-l+1 > w:
    if l not in discardElem:
        count[arrivals[l]] -= 1
    l += 1
```