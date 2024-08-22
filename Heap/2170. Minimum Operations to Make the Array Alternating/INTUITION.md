# Intuition

only top 2 frequency num matter.

find top 2 frequency element in both odd and even

odd: x1, x2 where # of x1 element > # of x2
even: y1, y1 where # of y1 > # of y2

# Approach

```
if x1 != y1:
    return n - (# of top1_odd) - (# of top1_even)
else:
    return min(
        n - (# of top1_odd + # of top2_even),
        n - (# of top2_odd + # of top1_even)
    )
```