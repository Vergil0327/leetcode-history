[3962. Maximum Subarray Sum After at Most K Swaps](https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/)

`Hard`

You are given an integer array nums and an integer k.

You are allowed to perform at most k swap operations on the array.

In one swap operation, you may choose any two indices i and j and swap nums[i] and nums[j].

Return an integer denoting the maximum possible subarray sum after performing the swaps.


Example 1:
Input: nums = [1,-1,0,2], k = 1
Output: 3
Explanation:
We can swap on indices 1 and 3, resulting in the array [1, 2, 0, -1].
The subarray [1, 2] has a sum of 3, which is the maximum possible subarray sum after at most k = 1​​​​​​​ swap.

Example 2:
Input: nums = [4,3,2,4], k = 2
Output: 13
Explanation:
The maximum possible subarray sum after at most k = 2 swaps is the sum of the entire array, which is 13.

Example 3:
Input: nums = [-1,-2], k = 0
Output: -1
Explanation:
k = 0 swaps are allowed.
The possible subarrays are [-1], [-2], and [-1, -2], with sums -1, -2, and -3 respectively.
Among these sums, the maximum is -1.
 

Constraints:

- 1 <= nums.length <= 1500
- -10^5 <= nums[i] <= 10^5
- 0 <= k <= nums.length

Accepted
1,355/14.5K
Acceptance Rate
9.4%

<details>
<summary>Hint 1</summary>

Fix a subarray. An optimal swap exchanges one of its smallest elements with one of the largest elements outside it, provided this increases the sum.

</details>
<details>
<summary>Hint 2</summary>

If the elements inside are ordered increasingly and those outside decreasingly, the gain from using t swaps is the sum of the t largest outside elements minus the sum of the t smallest inside elements.

</details>
<details>
<summary>Hint 3</summary>

Enumerate the left endpoint and extend the right endpoint while maintaining the inside and outside elements in order-statistics data structures that support counts, sums, and the sum of the smallest or largest t elements.

</details>
<details>
<summary>Hint 4</summary>

The marginal gains are non-increasing as t grows, so find the largest profitable t <= k and add its gain to the original subarray sum.

</details>