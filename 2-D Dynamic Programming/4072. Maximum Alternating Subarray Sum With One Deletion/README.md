[4072. Maximum Alternating Subarray Sum With One Deletion](https://leetcode.com/problems/maximum-alternating-subarray-sum-with-one-deletion/)

`Medium`

You are given an integer array nums.

You may delete at most one element from nums, then choose a subarray of the resulting array.

Return the maximum possible alternating sum of the chosen subarray.

The alternating sum of an array is the sum of its elements at even indices minus the sum of its elements at odd indices. The chosen subarray is reindexed starting from 0 before calculating its alternating sum.


Example 1:
Input: nums = [5,-5,1]
Output: 11
Explanation:
Choose not to delete an element and select the entire array. Its alternating sum is 5 - (-5) + 1 = 11, which is the maximum possible.

Example 2:
Input: nums = [10,-5,-100]
Output: 110
Explanation:
Delete nums[1] = -5 to obtain [10,-100], then select the entire resulting array. Its alternating sum is 10 - (-100) = 110, which is the maximum possible.

Example 3:
Input: nums = [4,7]
Output: 7
Explanation:
Choose not to delete an element and select the subarray [7]. Its alternating sum is 7, which is the maximum possible.

Constraints:

- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5

Accepted
7,931/26.8K
Acceptance Rate
29.6%

<details>
Hint 1
1a (Dynamic Programming): Track the maximum alternating sum of a non-empty candidate using two properties: the parity of its retained length and whether a deletion has been used.
</details>
<details>
Hint 2
1b (Dynamic Programming): Keeping the current element toggles the parity and adds or subtracts its value accordingly. Deleting it preserves the parity and uses the deletion. You can also start a new candidate with the current element.
</details>
<details>
Hint 3
2a (Prefix and Suffix Dynamic Programming): If the deleted element lies inside the chosen subarray, the remaining elements form a left segment followed by a right segment. The right segment begins with a minus sign when the left segment has odd length, and a plus sign otherwise.
</details>
<details>
Hint 4
2b (Prefix and Suffix Dynamic Programming): Precompute the best alternating sums of segments ending at each index for each length parity, and of segments starting at each index for each starting sign. Combine these across each possible deletion, and also consider the best subarray without deletion.
</details>