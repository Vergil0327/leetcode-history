# Intuition

Intuition

find max sum of subset where sum(A) = sum(B)
    height {X X X X} {X X X X} X
               A         B
                               i
                               not pick
                               pick X in A
                               pick X in B
    
    considering first i element, if we can make 2 subsets be sumA and sumB
    dp[i][sumA][sumB] = true/false # dp[i][left_rod_height][right_rod_height]
    dp[i][sumA][sumB] = dp[i-1][sumA-rods[i]][sumB] or dp[i-1][sumA][sumB-rods[i]] or dp[i-1][sumA][sumB]

but this would get TLE.

since what we only care is if we can make sumA = sumB, we don't really care any sumA with any sumB.

so, maybe we can use `difference` to represent this kind of dp state.

then we can turn `dp[sumA][sumB] where sumA == sumB` into `dp[diff] where diff = 0`,
and see if `dp[diff] = dp[0] = True or False`

we can define dp state as:

dp[i][diff]: the maximum height of **left** rod we can make where difference of left rod and right rod is `diff`, considering i-th selection, since height of left rod should equal right rod, we keep tracks of max height of left rod

because diff can be negative, we can use hashmap

```py
dp = [defaultdict(lambda: -inf) for _ in range(n+1)]
```

and state transfer fn should be:
- if we don't pick rods[i],  dp[i][diff] = dp[i-1][diff]
- if we pick rods[i] to left, dp[i][diff+rods[i]] = dp[i-1][diff] + rods[i]
- if we pick rods[i] to right, dp[i][diff-rods[i]] = dp[i-1][diff]

and each strategy we choose maximum

and the answer is `dp[n][0]`, considering n-th selection and diff is 0.

*p.s. if dp[i-1][diff] == -inf, we don't need to try updating dp state, just skip*

# Space-optimzed

since dp[i] only depends on dp[i-1],
we can use two hashmap `dp`, `prevdp` to transfer dp state

```py
dp = defaultdict(lambda: -inf)
prevdp = defaultdict(lambda: -inf)
prevdp[0] = 0

for i in range(1, n+1):
    for diff in range(-total, total+1):
        if prevdp[diff] == -inf: continue
        dp[diff] = max(dp[diff], prevdp[diff])
        dp[diff+rods[i]] = max(dp[diff+rods[i]], prevdp[diff] + rods[i])
        dp[diff-rods[i]] = max(dp[diff-rods[i]], prevdp[diff])
    dp, prevdp = prevdp, dp
return prevdp[0] if prevdp[0] != -inf else 0
```

# time-opimization

we can even optimize time complexity and space complexity

since we skip every prevdp[diff] == -inf, it means **we only update every key in hashset with value**

therefore, we can replace nested loop `for diff in range(-total, total+1)` with `prevdp.keys()`
and replace `dp` with `nxt = dp.copy()`, and replace `prevdp` with `dp`

now, we'll skip every invalid state and only iterate those valid state

```py
dp = defaultdict(lambda: -inf)
dp[0] = 0

for i in range(1, n+1):
    nxt = dp.copy()
    for diff in dp.keys():
        nxt[diff] = max(nxt[diff], dp[diff])
        nxt[diff+rods[i]] = max(nxt[diff+rods[i]], dp[diff] + rods[i])
        nxt[diff-rods[i]] = max(nxt[diff-rods[i]], dp[diff])
    dp = nxt
```