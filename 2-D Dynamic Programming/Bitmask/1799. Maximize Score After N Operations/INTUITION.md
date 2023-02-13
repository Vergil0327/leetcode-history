# bitmask DP (TLE for Python)

## Intuition

the scale is small, only `1 <= n <= 7`
if we want to find the maximum score of n operations, we must try every possible combination of x and y.

maximum nums.legnth is 14 at most, we can use 14-bit bitmask like `00000000000000` to represent the state whether the nums[i] has already used or not.

and we can think it as knapsack problem:

`dp[i][nums_state]: the maximum score when we consider first i nums with num_state`

and the **state transfer** fn should be:

iterate through all the nums with `step=2` since we must pair up values to get GCD

ex. state is `1111` and curr state we choose is `1010` which means we choose gcd(nums[1], nums[3])
since `1010` is subset of `1111`, we can transfer state from `0101+1010` to `1111`

```python
for i in range(0, n, 2):
    for nums_state in range(1<<n):
        find all the valid curr state:
            dp[i][nums_state] = max(dp[i][nums_state], dp[i-2][nums_state-curr] + (i//2) * getScores(curr))
```

we can use *Gosper's hack* to find m-1-bit in n-bit state

```py
state = (1<<m)-1

while state < (1<<n):
    # do something

    c = state & -state
    r = state+c
    state = (((r^state)>>2)//c) | r
```

**Base Case**
and we can append 2 more columns in front of dp array and the base case is:

`dp[0][0] = 0` and `dp = [[-inf]*(1<<n) for _ in range(n+2)]`

# Optimization

but we can see that this part still cost lots of time to compute.

thus, we can do something to reduce invalid states

```py
for nums_state in range(1<<n):
    if state != 0 and bin(state).count("1")%2 != 0: continue
    curr = (1<<m)-1
    while curr < maxState:
        if curr&state == curr:
            dp[i][state] = max(dp[i][state], dp[i-2][state-curr] + (i//2)*scores[curr])

        c = curr & -curr
        r = curr+c
        curr = (((r^curr)>>2)//c) | r
```

1. find valid num_state

since num_state is only valid when 1-bits is even or `0`, thus we can precompute valid state first

```py
validStates = []
for state in range(1<<n):
    if state != 0 and bin(state).count("1")%2 != 0: continue
    validStates.append(state)
```

and we can also precompute the subset of each valid state!!!

```py
validStates = []
possibleSubstates = defaultdict(list)
maxState = 1<<n
for state in range(maxState):
    if state != 0 and bin(state).count("1")%2 != 0: continue
    validStates.append(state)

    # Gosper's hack
    curr = (1<<m)-1
    while curr < maxState:
        if curr&state == curr:
            possibleSubstates[state].append(curr)

        c = curr & -curr
        r = curr+c
        curr = (((r^curr)>>2)//c) | r
```

and now, our core dp state transfer fn becomes:

```py
for i in range(2, n+2, 2):
    for state in validStates:
        for curr in possibleSubstates[state]:
            dp[i][state] = max(dp[i][state], dp[i-2][state-curr] + (i//2)*scores[curr])

return dp[n][(1<<n)-1]
```

the final result should be dp[n][(1<<n)-1] which means first n nums and select all the pairs

final result: beats 5%