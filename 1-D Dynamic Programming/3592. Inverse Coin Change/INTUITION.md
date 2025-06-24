# Intuition

`numWays` is a list where `numWays[i]` represents the number of ways to form the value `i` using coins. The goal is to find the coin denominations that can be used to achieve these counts.

now, what we need to do is to reverse engineer the process of forming these counts. We will iterate through the `numWays` list and for each non-zero count, we will determine the coin denomination that corresponds to that count.

we know that every numWays[i] > 1 is from the combination of previous coins, therefore, we can iterate all the `numWays[i] == 1` first and substract all the numWays[i:] by `numsWays[i]`.

if everything is fine, numWays will become all zero, otherwise, we will return an empty list.


time: O(n^2)
