# Intuition - first try

try greedy first

- sort by end_time to find as much non-overlapping interval as we can
- then sort earning in descending order
- pick up passenger as much as we can
can it work? no
```
ex.
[0,2,5],[2,4,5],[2,4,3]
[0,4,15]
```

since tip can influence how we pick, we can't greedily pick larger earning or as many passengers as possible.
pick up each passenger is a state, and how we pick depends on previous state
=> try dp

```
|->->|
  dp[end-1]

  |->->->->|
start   end
```

`dp[end] = max(dp[end-1], dp[previsou_interval_before_start] + earning)`

dp[end-1] is the closest interval but its end_time is smaller than current dp value
we can use `j = bisect_right(end)-1` to find dp[end-1] interval, i.e. dp[j]

SortedDict is a nice choice for us to store every dp value
we can think this SortedDict is an monotonic increasing hashmap
but we can just use dp array.

# Optimization

實際上延續我們上面的分析

我們用`dp = [0] * (n+1)`並定義:
`dp[t]: the maximum earning until time t `

那麼狀態轉移為:
- if we doesn't pick up passenger:
  - dp[t] = dp[t-1]
- if we pick up passenger:
  - dp[end_time] = max(dp[start], dp[start] + end-start+tip)
  - 但要注意同個時間點可能有多個乘客, 我們選最多錢的來載.
    - 可以用個雙指針來追蹤乘客
    

```py
def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
    dp = [0] * (n + 1)
    rides.sort(key=lambda x: x[1])

    j = 0
    for t in range(1, n + 1):
        dp[t] = dp[t-1]
        while j < len(rides) and t == rides[j][1]:
            start, end, tip = rides[j]
            dp[t] = max(dp[t], dp[start] + (end - start + tip))
            j += 1

    return dp[n]
```