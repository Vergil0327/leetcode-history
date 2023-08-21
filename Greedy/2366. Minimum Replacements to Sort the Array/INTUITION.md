# Intuition

first of all, operation only makes nums[i] smaller
=> which also means last element be greatest

thus, we shuold check reversely and make nums[i] smaller to satisfy non-decreasing order

```
nums = X X X X X nums[i] [nums[i+1] X X X X X X X X X X X]
                                      sorted
```

if nums[i+1:] already sorted, range of nums[i] must <= nums[i+1]
- if nums[i] <= nums[i+1], just keep it and continue iteration
- if nums[i] > nums[i+1], we should break nums[i] up into ***values*** and these *values* should as large as possible
    - one way to break is num[i] = k*nums[i+1] + nums[i]%nums[i+1]. this is the **fewest** operation to break up nums[i], see example 1.

but we'll fail at testcase below. if we break up 7 into 1+6, 1 is too small and it'll make rest of nums[:i-1] need more operations.

```
ex. [12,9,7,6,17,19], expected 6
 [12],  [9],  [7], 6, 17, 19
        6 3   3,4
       3 3
  6 6
3 3 3 3

7 -> 3,4
9 -> 6, 3 -> 3,3,3
12 -> 6,6 -> 6,3,3 -> 3,3,3,3
```

thus, we should also break up nums[i] into almost equally large pieces by fewest operation where fewest opration equals k = nums[i]//nums[i+1] times.

`nums[i] = k * nums[i+1] + remain`
we should make remain as large as possible, therefore, we can take some from k*nums[i+1]

```
nums[i] = remain + k * nums[i+1] = remain + X + X + X + X + X where X = nums[i+1]

nums[i], nums[i+1] = (remain, X X X ...), nums[i+1]
                   = (remain+k, X-1, X-1, X-1, ...), nums[i+1]
                   = (remain + k*some, X-some, X-some, X-some, ...), nums[i+1]
thus -> remain+k*some <= X-some
     -> some <= (X-remain)/(k+1)
        -> remain = remain+k*some
        -> X = X-some
```

if we can equally split, `remain = X-some`

if we can't, don't forget that we should make remain as large as possible.
if `remain' = remain+k*some < X-some`, we should be able to make `remain' == X-some-1` by take more from those k pieces.

```
remain+k*some, X-some, X-some, X-some, X-some, X-some

if remain+k*some < X-some, we can make break up like below, take m pieces to make remain = remain+k*some + m = X-some-1. and this is the largest possible remain

remain+k*some + m, {X-some-1, X-some-1, X-some-1}, X-some, X-some
                              m pieces
```

summary:
- we always break up nums[i] in fewest oprations:
    - if nums[i]%nums[i+1] == 0, totally nums[i]//nums[i+1] pieces => nums[i]//nums[i+1]-1 split
    - if nums[i]%nums[i+1] != 0, totally nums[i]//nums[i+1]+1 pieces => nums[i]//nums[i+1] split
- break up nums[i] into remain as largest as possible