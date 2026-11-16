[4114. Count Consistent Subarrays II](https://leetcode.com/problems/count-consistent-subarrays-ii/)

`Hard`

You are given an integer array nums.

A subarray is called consistent if the bitwise AND of all its elements is equal to the minimum value of the subarray.

Return the number of consistent subarrays in nums.

Example 1:
Input: nums = [5,3,1,2]
Output: 6
Explanation:

The following subarrays are consistent:

Subarray	Values	Bitwise AND	Minimum Value
nums[0..0]	[5]	5	5
nums[1..1]	[3]	3	3
nums[2..2]	[1]	1	1
nums[3..3]	[2]	2	2
nums[1..2]	[3, 1]	3 AND 1 = 1	1
nums[0..2]	[5, 3, 1]	5 AND 3 AND 1 = 1	1
Therefore, the number of consistent subarrays is 6.

Example 2:
Input: nums = [1,1,1]
Output: 6
Explanation:
For every subarray, both the bitwise AND and the minimum value are equal to 1. Therefore, the answer is 6.

Example 3:
Input: nums = [0]
Output: 1
Explanation:

The only subarray is [0], whose bitwise AND and minimum value are both 0. Therefore, the answer is 1.

Constraints:

- 1 <= nums.length <= 2 * 10​​​​​​​^5
- 0 <= nums[i] <= 10^6

Accepted
6,786/15.9K
Acceptance Rate
42.7%

<details>
<summary>Hint 1</summary>
1a (Distinct Suffix ANDs): The bitwise AND of a subarray is at most every element in it. Therefore, it equals the minimum exactly when the AND itself occurs in the subarray.

</details>
<details>
<summary>Hint 2</summary>
1b (Distinct Suffix ANDs): Fix the right endpoint and move the start left. Each change in the AND clears at least one bit, so the starting positions split into only a few ranges of equal AND. To advance the right endpoint, AND each range's value with the new element, add the singleton, and merge adjacent ranges with equal values.

</details>
<details>
<summary>Hint 3</summary>
1c (Distinct Suffix ANDs): Suppose starts in [a, b] give AND x. Among them, count the starts at or before the most recent occurrence of x. If x has not appeared, this range contributes zero.

</details>
<details>
<summary>Hint 4</summary>
2a (Monotonic Stack): Assign each consistent subarray to its leftmost minimum at index i. Every element in it must contain every set bit of nums[i]. How far can the subarray extend on either side of i?

</details>
<details>
<summary>Hint 5</summary>
2b (Monotonic Stack): On each side, stop at the nearest element missing a required bit. On the left, an equal value also stops the extension. If the stopping indices are L and R, index i contributes (i - L) * (R - i) subarrays. Use -1 and n for missing boundaries.

</details>
<details>
<summary>Hint 6</summary>
2c (Monotonic Stack): Scan from left to right with a stack of indices waiting for their right boundary. While the current value lacks a set bit of the top value, pop the top and assign its boundary. Then push the current index. The surviving masks form a chain by bit inclusion, so checking the top is enough. Scan in reverse for left boundaries, also popping equal values.

</details>