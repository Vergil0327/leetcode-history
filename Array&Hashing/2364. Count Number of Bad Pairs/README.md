[2364. Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs/)

`Medium`

You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

```
Example 1:
Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.
``` 

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9

Accepted
32K
Submissions
76.7K
Acceptance Rate
41.7%

<details>
<summary>Hint 1</summary>

Would it be easier to count the number of pairs that are not bad pairs?

</details>

<details>
<summary>Hint 2</summary>

Notice that (j - i != nums[j] - nums[i]) is the same as (nums[i] - i != nums[j] - j).

<details>

</details>
<summary>Hint 3</summary>

Keep a counter of nums[i] - i. To be efficient, use a HashMap.

</details>