[1191. K-Concatenation Maximum Sum](https://leetcode.com/problems/k-concatenation-maximum-sum/)

`Medium`

Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

```
Example 1:
Input: arr = [1,2], k = 3
Output: 9

Example 2:
Input: arr = [1,-2,1], k = 5
Output: 2

Example 3:
Input: arr = [-1,-2], k = 7
Output: 0
``` 

Constraints:

- 1 <= arr.length <= 10^5
- 1 <= k <= 10^5
- -10^4 <= arr[i] <= 10^4

Accepted
37.3K
Submissions
155.4K
Acceptance Rate
24.0%

<details>
<summary>Hint 1</summary>

How to solve the problem for k=1 ?

</details>
<details>
<summary>Hint 2</summary>

Use Kadane's algorithm for k=1.

</details>
<details>
<summary>Hint 3</summary>

What are the possible cases for the answer ?

</details>
<details>
<summary>Hint 4</summary>

The answer is the maximum between, the answer for k=1, the sum of the whole array multiplied by k, or the maximum suffix sum plus the maximum prefix sum plus (k-2) multiplied by the whole array sum for k > 1.

</details>