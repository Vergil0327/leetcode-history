# Intuition

```
steam = {... X X X X X X X X X} -> once steam.length >= m,  m elements to sorted container -> {Y Y Y Y Y ... [X X X X X X X X X X ]} -> remove k smallest and k largest
```

first of all: if steam.length < m, just return -1.

once steam.length >= m:
  - move last `m` elements to container and remove `k` smallest and `k` largest
    - maybe use sorted list?
    - but before sorting, we should know what these `m` last elements
    - at the same time, should calculate average just after remove these two `k` elements => maintain current sum

we need to keep steam in chronological order to find `m` last elements => m-size deque window
and maintain 3 k-length sorted list, one for smallest, another for largest, the other for middle

since we want MK average, maintain sum of m-size window `sum` and 2 k-length sorted list, `m1`, `m2`

MK Average = (sum - m1 - m2) / (m - 2*k)

ok, then we try to update steam, k-smallest and k-largest:

```
steam = {k small , ......, k large} X
```

so, if new element is `X`
- check if we need to popleft steam window: steam.popleft if steam.length >= m
    - Y = steam.popleft()
        - if Y in k-smallest:
            - update `sum` and `m1`
            - don't forget to balance k-smallest if k-smallest.length < k and we have some elements in **middle**
                - add middle[0] to k-smallest
                
        - if Y in k-largest:
            - update `sum` and `m2`
            - don't forget to balance k-largest if k-largest.length < k and we have some elements in **middle**
                - add middle[-1] to k-largest

        - else, it should exist in middle:
            - update `sum` and just pop out from middle
- put into k-small first
- once k-small is full, put in to k-large
- once both are full, check where should the new element `X` belong

```
{k-small[0] ... k-small[-1]} {middle[0] ... middle[-1]} {k-large[0] ... k-large[-1]}

add X to k-small -> pop k-small[-1]
    -> if k-large not full -> put into k-large
    -> if k-large full:
        -> if k-small[-1] <= k-large[0], done. put into middle
        -> if k-small[-1] > k-large[0] -> put into k-large and pop k-large[0] into middle

    -> or we just put into k-large directly and pop k-large[0] into middle if k-large.length > k
```