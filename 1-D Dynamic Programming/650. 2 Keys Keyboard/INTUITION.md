# Top-Down DP

## Intuition

let's simulate the typing process

1. 1 character with 0 copy
  - we can copy current 1 character and must paste at next step. it's meaningless to copy and don't paste
  - it's meaningless to paste if we don't have a copy

2. either copy or paste but still follow rule below
   - if we copy, we must paste at next step or we'll waste steps & can't achieve minimum step
   - if we paste, we must have already copy some characters or we'll waste steps for only copying and can't achieve minimum

thus, we know our decision tree and we can DFS to find the result

define `DFS(current characters on the screen, copy we hold currently)` to return **minimum steps** for us to achieve `n` characters

- for operation `copy`:

```python
steps = dfs(characters+characters, characters) + 2 # 2 steps at least
```

- for operation `paste`

```python
if copy > 0:
    steps = dfs(characters+copy, copy) + 1
```

## Complexity

- time complexity:

$$O(n*n)$$

- space complexity:

$$O(n*n)$$

# Bottom-Up

## Intuition

**DP definition**

`dp[i]: the minimum operations to achieve i character`

**Base Case**

- `dp[1] = 0`:
1 character on the screen in the beginning, 0 operation
- since we want minimum operations, set `inf` as default value

**State Transfer Operation**

1. copy first 1 character and paste afterwards

```python
for i in range(2, n+1):
    dp[i] = i
```

ex. n = 2, copy, paste
ex. n = 3, copy, paste, paste
ex. n = 4, copy, paste, paste, paste
...

2. try every possible `copy`

`copy` from 1 to i means `A`, to `A.....A` where length is i

if `copy` is 1, `copy + paste + paste...` will be `i//1` times totally

```
ex. i = "AAAA", copy="AA"

- copy "AA"
- paste "AA"
total 2 operations
```

```python
for i in range(2, n+1):
    for copy in range(1, i+1):
        if i%copy == 0:
            times = i//copy
            dp[i] = min(dp[i], dp[copy]+times)
```

**Optimized**

for `i` characters, we can find `copy` from `i-1` to `2` reversely.

the optimal way to get is copy as large as possible and paste in minimum times