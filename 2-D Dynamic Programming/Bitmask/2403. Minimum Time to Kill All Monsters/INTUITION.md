# Intuition

the concepts of both top-down and bottom-up are the same

since `1 <= power.length <= 17`, we can use bitmast to represent the monster we've defeated

ex. `001001` means we've defeated power[0] and power[3]

$2^17$ = 131072 ~ $10^5$

and the days we need to defeat only depends on previous state

days we need to defeat current round's monster is:

`ceil(power[i]/(1+how many monster we've already defeated))`

thus, we can define `dp` as:

dp[state]: the minimum number of days needed to defeat this `state`

and state transfer is:

`dp[state] = min(dp[state], dp[state-current_state] + daysNeed)`

ex. if this round choose to defeat power[i]
dp[state] = min(dp[state], dp[state-(1<<i)] + daysNeedToDefeat[i])

**base case**

dp[0] = 0, the minimum time to defeat 0 monster is 0