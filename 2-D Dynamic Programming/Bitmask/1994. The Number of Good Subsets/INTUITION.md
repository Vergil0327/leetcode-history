# Intuition

change each nums[i] to be its factors such as 15 = 3*5 and use bitmask to represent like 15 = 101000

if one bitmask is not the other's submask, we can call it good subset.
also if nums[i] itself can't be represented as distinct bitmask, it can't be candidate to pick, ex. 4 = 2 * 2 -> not good

thus, we can filter nums[i] and only leave goot nums[i] which can be represented as product of distinct factors.

since nums[i] <= 30, all the possible good_nums are [2,3,5,6,7,11,13,14,15,17,19,21,22,23,26,29,30]
total number of good nums is 18 -> maximum number of good subset is $2^18$

```
def findValidNum(nums):
    valids = []
    for num in nums:
        if num <= 2:
            valids.append([num])
            continue

        factors = []
        factor = 2
        invalid = False
        while factor <= num and num > 0:
            while num % factor == 0 and num > 1:
                if factors and factors[-1] == factor: # only distinct factor is valid
                    invalid = True
                    break
                factors.append(factor)
                num //= factor
            if invalid: break

            factor += 1
        if not invalid:
            valids.append(factors)
    return valids

goodNums = findValidNum(nums)
for state in range(1<<len(godNums)):
    if state is valid: # no duplicate prime
        choices of current state = findChooseNums(state)
        res += count[choice_1] * count[choice_2] * count[choice_3] * ... 

return res * (2**count[1])
```

but we can think further. since the definition of good subset contains `distinct prime factor` only, we can think only prime factors which is [2,3,5,7,11,13,17,19,23,29]. 10 prime factors only.

so, there are 2^10 possible combinations to form a good subset.

if current subset is dp[{2,3,5}], it can be transfered from dp[{2,3}] with dp[{5}]
thus, if current dp state is dp[{2,3}]=6 and current nums[i] is 5, it means we have 6 ways to construct dp[{2,3,5}] state.
if we have 9 duplicate nums[i], it means we have 6 * 9 ways to construct dp[{2,3,5}] state.

this is dynamic programming knapsack problem.

```py
for num in nums:
    nextDp = []
    for state in range((1<<n)):
        if num is substate of state:
            nextDp[state] += dp[state-subset] * count[num]
    dp = nextDp

# or update dp state reversely to reuse dp array
for num in nums:
    for state in range((1<<n)-1, 0, -1):
        if num is substate of state:
            dp[state] += dp[state-subset] * count[num]
```

after we update our dp state, the number of goodset `WITHOUT` 1 is sum(dp[state]):
and for every good subset, if we have four `1` in nums, we add one `1` to each good subset or two `1` or three `1` or four `1` to each good subset.
after we add some `1` to each good subset, each subset is still a good subset.

ex. 1 `1` has 2^1 ways to add to each substate of  dp[{2,3,5}] -> dp[{2,3}], dp[{5}]
                                                                  -> dp[{1,2,3}], dp[{5}]
                                                                  -> dp[{2,3}], dp[{1,5}]
 
thus, total good subset is `sum(dp[state]) * (2**count[1]) where dp state is 1 to 1<<n`.

we can't just sum(dp). dp[0] is invalid because `0` means empty subset.
thus total good subset is:

```py
total = 0
for state in range(1, 1<<n):
    total += dp[state]
total *= (2**count[1])
total %= int(1e9+7)
```
