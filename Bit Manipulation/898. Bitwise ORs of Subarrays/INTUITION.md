# Intuition

see constraint:

- arr[i] <= 10^9
- 2^32 = 4294967296 >= 4 * 10^9

therefore, we can use 32 bit to store arr[i]

subarray = [l:r] must end at one of index from 0 to n-1

dp[i]: the possible distinct bitwise ORs of subarrays ended at arr[i]

** state transfer fn**
must pick arr[i]: `dp[i] = {prev in dp[i-1]} OR arr[i]`

so, we can iterate every arr[i] to calculate dp[i] and we'll know all the possible subarrays,
and we can add all of them into **answer** hashset

final answer = len(answer)

why this works?
=> len(dp) <= 32, 32 different bit position to OR at most

no matter what number in dp[i-1], 00000, 000001, 000010, 000100, 001000, ..., 1000...
think arr[i] = 00000...1 as a mask

for arr[i] **OR** {bit in dp[i-1]}, only 32 diffrent result bitmask at most

# Complexity

- time complexity

$$O(32n)$$