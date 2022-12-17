# Top-Down DP

## Intuition

we have two set, `A` & `B`, and we want to make `sum(A) == sum(B)`

we can use `take or skip` strategy for DFS and keep tracking `diff` between `A` and `B`

## Approach

for every current i-th number, we can choose to put in `A` set or not.

if we put it in `A`, `diff+nums[i]`
if we skip it, which means we put it in `B`, `diff-nums[i]`

after we traverse all the `nums`, once we have `diff=0` it means we can partition `nums` into two equal subset

## Complexity

- time complexity:

$$O(N*DIFF)$$ with memorization

- space complexity:

$$O(N)$$

# Bottom-Up with Hashmap

## Intuition

we have two set, `A` & `B`, and we want to make `sum(A) == sum(B)`, and we know the *target sum* is `sum(nums)//2`

let's define dp[i] = True/False

if dp[i] = True, means we can make one set have `i` sum

after traversing all the nums array, we can get all the possible sum, then we check if `dp[target sum]` is **True** or **False**.

## Complexity

- time complexity:

$$O(N*SUM)$$ with memorization

- space complexity:

$$O(SUM)$$

# Bottom-Up: 0/1 knapsack problem

## Intuition

**define dp:**

`dp[i][j]`: can we use first i num to make sum equal to j.

**state transfer funcion:**

`dp[i][j] = dp[i-1][j] or dp[i-1][j-num]`
- if we we can put num into, dp[i][j] = dp[i-1][j-num]
- if we can't put num into, dp[i][j] = dp[i-1][j]

## Complexity

- time complexity:

$$O(N*SUM)$$

- space complexity:

$$O(N*SUM)$$

## Space-optimized

**Intuition**

we can see that `dp[i][j]` only depends on `dp[i-1][...]`, only depends on previous `dp` state.

thus, we can reduce space complexity by using only 1-D array `dp[j]`.

Also, we can see that since `dp[i][j] = dp[i-1][j] or dp[i-1][j-num]`, which means `dp[j] = prevDp[j] or prevDp[j-num]`

at current iteration, if we iterate sum reversely, we can reuse current `dp[j]` array rather than using two dp array, `dp[j]` and `prevDp[j]`.

thus, space complexity can reduce to `O(SUM)`