[3413. Maximum Coins From K Consecutive Bags](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/description/)

`Medium`

There are an infinite amount of bags on a number line, one bag for each coordinate. Some of these bags contain coins.

You are given a 2D array coins, where coins[i] = [li, ri, ci] denotes that every bag from li to ri contains ci coins.

The segments that coins contain are non-overlapping.

You are also given an integer k.

Return the maximum amount of coins you can obtain by collecting k consecutive bags.

```
Example 1:
Input: coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4
Output: 10
Explanation:

Selecting bags at positions [3, 4, 5, 6] gives the maximum number of coins: 2 + 0 + 4 + 4 = 10.

Example 2:
Input: coins = [[1,10,3]], k = 2
Output: 6
Explanation:

Selecting bags at positions [1, 2] gives the maximum number of coins: 3 + 3 = 6.
```

Constraints:

- 1 <= coins.length <= 10^5
- 1 <= k <= 10^9
- coins[i] == [li, ri, ci]
- 1 <= li <= ri <= 10^9
- 1 <= ci <= 1000
- The given segments are non-overlapping.

Accepted
3K
Submissions
16.8K
Acceptance Rate
17.9%

<details>
<summary>Hint 1</summary>
An optimal starting position for k consecutive bags will be either `li` or `ri - k + 1`.
</details>