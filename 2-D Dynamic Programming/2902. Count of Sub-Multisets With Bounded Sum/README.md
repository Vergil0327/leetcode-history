[2902. Count of Sub-Multisets With Bounded Sum](https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/)

`Hard`

You are given a 0-indexed array nums of non-negative integers, and two integers l and r.

Return the count of sub-multisets within nums where the sum of elements in each subset falls within the inclusive range of [l, r].

Since the answer may be large, return it modulo 109 + 7.

A sub-multiset is an unordered collection of elements of the array in which a given value x can occur 0, 1, ..., occ[x] times, where occ[x] is the number of occurrences of x in the array.

Note that:

Two sub-multisets are the same if sorting both sub-multisets results in identical multisets.
The sum of an empty multiset is 0.
 
```
Example 1:
Input: nums = [1,2,2,3], l = 6, r = 6
Output: 1
Explanation: The only subset of nums that has a sum of 6 is {1, 2, 3}.

Example 2:
Input: nums = [2,1,4,2,7], l = 1, r = 5
Output: 7
Explanation: The subsets of nums that have a sum within the range [1, 5] are {1}, {2}, {4}, {2, 2}, {1, 2}, {1, 4}, and {1, 2, 2}.

Example 3:
Input: nums = [1,2,1,3,5,2], l = 3, r = 5
Output: 9
Explanation: The subsets of nums that have a sum within the range [3, 5] are {3}, {5}, {1, 2}, {1, 3}, {2, 2}, {2, 3}, {1, 1, 2}, {1, 1, 3}, and {1, 2, 2}.
``` 

Constraints:

- 1 <= nums.length <= 2 * 10^4
- 0 <= nums[i] <= 2 * 10^4
- Sum of nums does not exceed 2 * 10^4.
- 0 <= l <= r <= 2 * 10^4

Accepted
1.2K
Submissions
9.4K
Acceptance Rate
12.9%

<details>
<summary>Hint 1</summary>

Since the sum of numsis at most 20000, the number of distinct elements of nums is 200.

</details>
<details>
<summary>Hint 2</summary>

Let dp[x] be the number of submultisets of nums with sum x.

</details>
<details>
<summary>Hint 3</summary>

The answer to the problem is dp[l] + dp[l+1] + … + dp[r].

</details>
<details>
<summary>Hint 4</summary>

Use coin change dp to transition between states.

</details>