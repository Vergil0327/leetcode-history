[3670. Maximum Product of Two Integers With No Common Bits](https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/)

`Medium`

You are given an integer array nums.

Your task is to find two distinct indices i and j such that the product nums[i] * nums[j] is maximized, and the binary representations of nums[i] and nums[j] do not share any common set bits.

Return the maximum possible product of such a pair. If no such pair exists, return 0.

```
Example 1:
Input: nums = [1,2,3,4,5,6,7]
Output: 12
Explanation:
The best pair is 3 (011) and 4 (100). They share no set bits and 3 * 4 = 12.

Example 2:
Input: nums = [5,6,4]
Output: 0
Explanation:
Every pair of numbers has at least one common set bit. Hence, the answer is 0.

Example 3:
Input: nums = [64,8,32]
Output: 2048
Explanation:
No pair of numbers share a common bit, so the answer is the product of the two maximum elements, 64 and 32 (64 * 32 = 2048).
```

Constraints:

- 2 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6

Accepted
4,242/42.2K
Acceptance Rate
10.0%

<details>
<summary>Hint 1</summary>

Think of each number as a mask: treat nums[i] as a bitmask.

</details>
<details>
<summary>Hint 2</summary>

Create an array dp of size 1<B, where B is your bit‑width.

</details>
<details>
<summary>Hint 3</summary>

Initialize dp[mask] to the maximum nums[i] exactly equal to that mask, or 0 if none.

</details>
<details>
<summary>Hint 4</summary>

For each m, propagate to all its super‑masks M: dp[m] = max(dp[m], dp[M])

</details>
<details>
<summary>Hint 5</summary>

For a number x with mask mx, compute its "complement mask" as cm

</details>
<details>
<summary>Hint 6</summary>

The best disjoint partner is then dp[cm].

</details>
<details>
<summary>Hint 7</summary>

Loop over all x in nums, look up dp[cm], and track the maximum x * partner.

</details>