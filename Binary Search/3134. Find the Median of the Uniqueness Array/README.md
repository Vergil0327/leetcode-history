[3134. Find the Median of the Uniqueness Array](https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/)

`Hard`

You are given an integer array nums. The uniqueness array of nums is the sorted array that contains the number of distinct elements of all the subarrays of nums. In other words, it is a sorted array consisting of distinct(nums[i..j]), for all 0 <= i <= j < nums.length.

Here, distinct(nums[i..j]) denotes the number of distinct elements in the subarray that starts at index i and ends at index j.

Return the median of the uniqueness array of nums.

Note that the median of an array is defined as the middle element of the array when it is sorted in non-decreasing order. If there are two choices for a median, the smaller of the two values is taken.

```
Example 1:
Input: nums = [1,2,3]
Output: 1
Explanation:

The uniqueness array of nums is [distinct(nums[0..0]), distinct(nums[1..1]), distinct(nums[2..2]), distinct(nums[0..1]), distinct(nums[1..2]), distinct(nums[0..2])] which is equal to [1, 1, 1, 2, 2, 3]. The uniqueness array has a median of 1. Therefore, the answer is 1.

Example 2:
Input: nums = [3,4,3,4,5]
Output: 2
Explanation:

The uniqueness array of nums is [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]. The uniqueness array has a median of 2. Therefore, the answer is 2.

Example 3:
Input: nums = [4,3,5,4]
Output: 2
Explanation:

The uniqueness array of nums is [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]. The uniqueness array has a median of 2. Therefore, the answer is 2.
```

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5

Accepted
2.7K
Submissions
11.2K
Acceptance Rate
24.2%

<details>
<summary>Hint 1</summary>

Binary search over the answer.

</details>
<details>
<summary>Hint 2</summary>

For a given x, you need to check if x is the median, to the left of the median, or to the right of the media. You can do that by counting the number of sub-arrays nums[i…j] such that distinct(num[i…j]) <= x.

</details>
<details>
<summary>Hint 3</summary>

Use the sliding window to solve the counting problem in the hint above.

</details>