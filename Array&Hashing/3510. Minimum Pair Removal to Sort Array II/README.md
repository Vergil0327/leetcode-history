[3510. Minimum Pair Removal to Sort Array II](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/)

`Hard`

Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

```
Example 1:
Input: nums = [5,2,3,1]
Output: 2
Explanation:

The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
The array nums became non-decreasing in two operations.

Example 2:
Input: nums = [1,2,2]
Output: 0
Explanation:

The array nums is already sorted.
```

Constraints:

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Accepted
1.3K
Submissions
14.1K
Acceptance Rate
9.0%

<details>
<summary>Hint 1</summary>

We can perform the simulation using data structures.

</details>
<details>
<summary>Hint 2</summary>

Maintain an array index and value using a map since we need to find the next and previous ones.

</details>
<details>
<summary>Hint 3</summary>

Maintain the indices to be removed using a hash set.

</details>
<details>
<summary>Hint 4</summary>

Maintain the neighbor sums with the smaller indices (set or priority queue).

</details>
<details>
<summary>Hint 5</summary>

Keep the 3 structures in sync during the removals.

</details>
