[2659. Make Array Empty](https://leetcode.com/problems/make-array-empty/description/)

`Hard`

You are given an integer array nums containing distinct numbers, and you can perform the following operations until the array is empty:

If the first element has the smallest value, remove it
Otherwise, put the first element at the end of the array.
Return an integer denoting the number of operations it takes to make nums empty.

```
Example 1:
Input: nums = [3,4,-1]
Output: 5
Operation	Array
1	[4, -1, 3]
2	[-1, 3, 4]
3	[3, 4]
4	[4]
5	[]

Example 2:
Input: nums = [1,2,4,3]
Output: 5
Operation	Array
1	[2, 4, 3]
2	[4, 3]
3	[3, 4]
4	[4]
5	[]

Example 3:
Input: nums = [1,2,3]
Output: 3
Operation	Array
1	[2, 3]
2	[3]
3	[]
``` 

Constraints:

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- All values in nums are distinct.

Acceptance Rate
6.8%

<details>
<summary>Hint 1</summary>

Understand the order in which the indices are removed from the array.

</details>

<details>
<summary>Hint 2</summary>

We don’t really need to delete or move the elements, only the array length matters.

</details>

<details>
<summary>Hint 3</summary>

Upon removing an index, decide how many steps it takes to move to the next one.

</details>

<details>
<summary>Hint 4</summary>

Use a data structure to speed up the calculation.

</details>

<details>
<summary>Solution Explanation</summary>

[Lee215](https://leetcode.com/problems/make-array-empty/solutions/3466800/java-c-python-easy-sort-solution/)
</details>