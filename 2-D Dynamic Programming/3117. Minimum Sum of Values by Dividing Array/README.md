[3117. Minimum Sum of Values by Dividing Array](https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/)

`Hard`

You are given two arrays nums and andValues of length n and m respectively.

The value of an array is equal to the last element of that array.

You have to divide nums into m disjoint contiguous 
subarrays
 such that for the ith subarray [li, ri], the bitwise AND of the subarray elements is equal to andValues[i], in other words, nums[li] & nums[li + 1] & ... & nums[ri] == andValues[i] for all 1 <= i <= m, where & represents the bitwise AND operator.

Return the minimum possible sum of the values of the m subarrays nums is divided into. If it is not possible to divide nums into m subarrays satisfying these conditions, return -1.

```
Example 1:
Input: nums = [1,4,3,3,2], andValues = [0,3,3,2]
Output: 12
Explanation:

The only possible way to divide nums is:

[1,4] as 1 & 4 == 0.
[3] as the bitwise AND of a single element subarray is that element itself.
[3] as the bitwise AND of a single element subarray is that element itself.
[2] as the bitwise AND of a single element subarray is that element itself.
The sum of the values for these subarrays is 4 + 3 + 3 + 2 = 12.

Example 2:
Input: nums = [2,3,5,7,7,7,5], andValues = [0,7,5]
Output: 17
Explanation:

There are three ways to divide nums:

[[2,3,5],[7,7,7],[5]] with the sum of the values 5 + 7 + 5 == 17.
[[2,3,5,7],[7,7],[5]] with the sum of the values 7 + 7 + 5 == 19.
[[2,3,5,7,7],[7],[5]] with the sum of the values 7 + 7 + 5 == 19.
The minimum possible sum of the values is 17.

Example 3:
Input: nums = [1,2,3,4], andValues = [2]
Output: -1
Explanation:

The bitwise AND of the entire array nums is 0. As there is no possible way to divide nums into a single subarray to have the bitwise AND of elements 2, return -1.
```
 

Constraints:

- 1 <= n == nums.length <= 10^4
- 1 <= m == andValues.length <= min(n, 10)
- 1 <= nums[i] < 10^5
- 0 <= andValues[j] < 10^5

Accepted
1.6K
Submissions
7.7K
Acceptance Rate
20.8%

<details>
<summary>Hint 1</summary>

Let dp[i][j] be the optimal answer to split nums[0..(i - 1)] into the first j andValues.

</details>
<details>
<summary>Hint 2</summary>

dp[i][j] = min(dp[(i - z)][j - 1]) + nums[i - 1] over all x <= z <= y and dp[0][0] = 0, where x and y are the longest and shortest subarrays ending with nums[i - 1] and the bitwise-and of all the values in it is andValues[j - 1].

</details>
<details>
<summary>Hint 3</summary>

The answer is dp[n][m].

</details>
<details>
<summary>Hint 4</summary>

To calculate x and y, we can use binary search (or sliding window). Note that the more values we have, the smaller the AND value is.

</details>
<details>
<summary>Hint 5</summary>

To calculate the result, we need to support RMQ (range minimum query). Segment tree is one way to do it in O(log(n)). But we can use Monotonic Queue since the ranges are indeed “sliding to right” which can be reduced to the classical minimum value in sliding window problem, for a O(n) solution.

</details>