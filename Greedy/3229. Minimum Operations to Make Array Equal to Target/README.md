[3229. Minimum Operations to Make Array Equal to Target](https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/)

`Hard`

You are given two positive integer arrays nums and target, of the same length.

In a single operation, you can select any 
subarray
 of nums and increment or decrement each element within that subarray by 1.

Return the minimum number of operations required to make nums equal to the array target.

```
Example 1:
Input: nums = [3,5,1,2], target = [4,6,2,4]
Output: 2
Explanation:

We will perform the following operations to make nums equal to target:
- Increment nums[0..3] by 1, nums = [4,6,2,3].
- Increment nums[3..3] by 1, nums = [4,6,2,4].

Example 2:
Input: nums = [1,3,2], target = [2,1,4]
Output: 5
Explanation:

We will perform the following operations to make nums equal to target:
- Increment nums[0..0] by 1, nums = [2,3,2].
- Decrement nums[1..1] by 1, nums = [2,2,2].
- Decrement nums[1..1] by 1, nums = [2,1,2].
- Increment nums[2..2] by 1, nums = [2,1,3].
- Increment nums[2..2] by 1, nums = [2,1,4].
```

Constraints:

- 1 <= nums.length == target.length <= 10^5
- 1 <= nums[i], target[i] <= 10^8

Accepted
12.2K
Submissions
33K
Acceptance Rate
37.0%

<details>
<summary>Hint 1</summary>

Change nums'[i] = nums[i] - target[i], so our goal is to make nums' into all 0s.

</details>
<details>
<summary>Hint 2</summary>

Divide and conquer.

</details>

<details>
<summary>Hint</summary>

follow-up of [1526. Minimum Number of Increments on Subarrays to Form a Target Array](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/)
</details>