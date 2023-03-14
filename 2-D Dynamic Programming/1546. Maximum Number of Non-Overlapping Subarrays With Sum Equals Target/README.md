[1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)

`Medium`

Given an array `nums` and an integer `target`, return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.

```
Example 1:
Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).

Example 2:
Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
```

Constraints:

- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 0 <= target <= 10^6

<details>
<summary>Hint 1</summary>

Keep track of prefix sums to quickly look up what subarray that sums "target" can be formed at each step of scanning the input array.

</details>

<details>
<summary>Hint 2</summary>

It can be proved that greedily forming valid subarrays as soon as one is found is optimal.

</details>

<details>
<summary>Video Explanantion</summary>

[HuifengGuan](https://www.youtube.com/watch?v=-xcIbf0KSgs&ab_channel=HuifengGuan)
</details>
