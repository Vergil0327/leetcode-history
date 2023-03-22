# Intuition

Greedy Approach

for every team[i] == 0, it should match the closest and valid **it** (`team[i] == 1`)

```
team = XXXXXXXXX 0 XXX 1 XXX 1 XXX
```

once `it` matched with `0`, it can't be caught again.

thus, we can use tow pointers `i` & `j`
we can iterate i and whenever `team[i] = 1`, we found left-most `0` in [i-dist,i+dist]
since both `i` and `j` only go forward to right, the time complexity should be O(n)