[4033. Valid K-Unique Subarrays I](https://leetcode.com/problems/valid-k-unique-subarrays-i/)

`Hard`

You are given an integer array nums and an integer k.
You are also given a 2D integer array queries, where queries[i] = [li, ri] represents the subarray nums[li..ri].
For each query, the subarray nums[li..ri] is considered valid if:

- It contains exactly k distinct numbers, and
- The frequency of every number in the subarray is even.
Return a boolean array ans, where ans[i] is true if nums[li..ri] is valid, and false otherwise.

Example 1:
Input: nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]
Output: [false,true,false]
Explanation:

i	[li, ri]	Subarray	Unique numbers	Frequency	Validity check
0	[0, 1]	[1, 2]	{1, 2} → 2	{1: 1, 2: 1}	false: Element counts are not even.
1	[0, 3]	[1, 2, 2, 1]	{1, 2} → 2	{1: 2, 2: 2}	true: Exactly k = 2 distinct elements, all appear an even number of times.
2	[1, 2]	[2, 2]	{2} → 1	{2: 2}	false: Number of distinct elements is less than k = 2.
Thus, ans = [false, true, false].

Example 2:
Input: nums = [3,3,3], k = 1, queries = [[1,2],[0,2]]
Output: [true,false]
Explanation:

i	[li, ri]	Subarray	Unique numbers	Frequency	Validity check
0	[1, 2]	[3, 3]	{3} → 1	{3: 2}	true: Exactly k = 1 distinct element, appears an even number of times.
1	[0, 2]	[3, 3, 3]	{3} → 1	{3: 3}	false: 3 does not appear an even number of times.
Thus, ans = [true, false].

Constraints:

- 2 <= n == nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= n
- 1 <= queries.length <= 10^5
- queries[i] == [li, ri]
- 0 <= li < ri <= n - 1

Accepted
1,701/18.6K
Acceptance Rate
9.1%

<details>
<summary>Hint 1</summary>

Process the queries offline using Mo’s algorithm so that the current subarray can be adjusted one element at a time.

</details>
<details>
<summary>Hint 2</summary>

Maintain both the number of distinct values and the number of values having an odd frequency. A query is valid exactly when these quantities are k and 0, respectively.

</details>