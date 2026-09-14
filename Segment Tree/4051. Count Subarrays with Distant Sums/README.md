[4051. Count Subarrays with Distant Sums](https://leetcode.com/problems/count-subarrays-with-distant-sums/)

`Hard`

You are given an integer array nums and two integers goal and k.

A subarray nums[i..j] is considered distant if the absolute difference between its sum and goal is at least k.

Return the number of distant subarrays.

Example 1:
Input: nums = [1,2,1], goal = 4, k = 1
Output: 5
Explanation:

The distant subarrays for k = 1 are:

i	j	nums[i..j]	Sum	abs(sum - goal)
0	0	[1]	1	3
1	1	[2]	2	2
2	2	[1]	1	3
0	1	[1, 2]	3	1
1	2	[2, 1]	3	1
Thus, the answer is 5.

Example 2:
Input: nums = [2,-1,3], goal = 2, k = 2
Output: 2
Explanation:
The distant subarrays for k = 2 are:

i	j	nums[i..j]	Sum	abs(sum - goal)
1	1	[-1]	-1	3
0	2	[2, -1, 3]	4	2
Thus, the answer is 2.

Example 3:
Input: nums = [-3,1,2], goal = 0, k = 3
Output: 2
Explanation:
The distant subarrays for k = 3 are:

i	j	nums[i..j]	Sum	abs(sum - goal)
0	0	[-3]	-3	3
1	2	[1, 2]	3	3
Thus, the answer is 2.


Constraints:

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- -10^9 <= goal <= 10^9
- 0 <= k <= 10^9

Accepted
4,013/13K
Acceptance Rate
31.0%

<details>
<summary>Hint 1</summary>
1a (Fenwick Tree). If k = 0, every subarray is distant. Otherwise, for a current prefix sum s and an earlier prefix sum p, the subarray is distant when p <= s - goal - k or p >= s - goal + k.


</details>
<details>
<summary>Hint 2</summary>
1b (Fenwick Tree). Compress the prefix sums and process them from left to right. Use a Fenwick tree to count earlier prefix sums in these two ranges, querying before inserting the current prefix sum.


</details>
<details>
<summary>Hint 3</summary>
2a (Merge Sort). Count the complementary subarrays whose sums satisfy goal - k < sum < goal + k, then subtract this count from n * (n + 1) / 2. Handle k = 0 directly.


</details>
<details>
<summary>Hint 4</summary>
2b (Merge Sort). Apply merge sort to the prefix sums. At each merge, use two pointers across the sorted halves to count differences strictly between the two bounds.


</details>