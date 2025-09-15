[3686. Number of Stable Subsequences](https://leetcode.com/problems/number-of-stable-subsequences/)

`Hard`

You are given an integer array nums.

A subsequence is stable if it does not contain three consecutive elements with the same parity when the subsequence is read in order (i.e., consecutive inside the subsequence).

Return the number of stable subsequences.

Since the answer may be too large, return it modulo $10^9$ + 7.

```
Example 1:
Input: nums = [1,3,5]
Output: 6
Explanation:

Stable subsequences are [1], [3], [5], [1, 3], [1, 5], and [3, 5].
Subsequence [1, 3, 5] is not stable because it contains three consecutive odd numbers. Thus, the answer is 6.

Example 2:
Input: nums = [2,3,4,2]
Output: 14
Explanation:

The only subsequence that is not stable is [2, 4, 2], which contains three consecutive even numbers.
All other subsequences are stable. Thus, the answer is 14.
```

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10​​​​​​​^5
 

Accepted
6,627/13.6K
Acceptance Rate
48.9%

<details>
<summary>Hint 1</summary>

Any subsequence of length 1 or 2 is always stable.

</details>
<details>
<summary>Hint 2</summary>

A subsequence becomes invalid only if you add a third consecutive element of the same parity.

</details>
<details>
<summary>Hint 3</summary>

Use DP tracking the last element’s parity and how many consecutive of that parity you have (1 or 2).

</details>
<details>
<summary>Hint 4</summary>

For each new number, either start a new subsequence, extend with same parity (if count < 2), or extend with different parity (reset count = 1).

</details>