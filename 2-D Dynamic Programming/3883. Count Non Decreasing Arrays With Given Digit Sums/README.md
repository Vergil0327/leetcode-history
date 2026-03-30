[3883. Count Non Decreasing Arrays With Given Digit Sums](https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/)

`Hard`

You are given an integer array digitSum of length n.

An array arr of length n is considered valid if:

- 0 <= arr[i] <= 5000
- it is non-decreasing.
- the sum of the digits of arr[i] equals digitSum[i].

Return an integer denoting the number of distinct valid arrays. Since the answer may be large, return it modulo $10^9 + 7$.

An array is said to be non-decreasing if each element is greater than or equal to the previous element, if it exists.


Example 1:
Input: digitSum = [25,1]
Output: 6
Explanation:
Numbers whose sum of digits is 25 are 799, 889, 898, 979, 988, and 997.

The only number whose sum of digits is 1 that can appear after these values while keeping the array non-decreasing is 1000.

Thus, the valid arrays are [799, 1000], [889, 1000], [898, 1000], [979, 1000], [988, 1000], and [997, 1000].

Hence, the answer is 6.

Example 2:
Input: digitSum = [1]
Output: 4
Explanation:
The valid arrays are [1], [10], [100], and [1000].

Thus, the answer is 4.

Example 3:
Input: digitSum = [2,49,23]
Output: 0
Explanation:

There is no integer in the range [0, 5000] whose sum of digits is 49. Thus, the answer is 0.

Constraints:

- 1 <= digitSum.length <= 1000
- 0 <= digitSum[i] <= 50
 

Accepted
4,362/10.1K
Acceptance Rate
43.3%

<details>
<summary>Hint 1</summary>

Use dynamic programming

</details>
<details>
<summary>Hint 2</summary>

Group every number from 0 to 5000 by its digit sum into sorted vectors once.

</details>
<details>
<summary>Hint 3</summary>

dp[j] holds the number of ways ending exactly at the j-th candidate for the current position.

</details>
<details>
<summary>Hint 4</summary>

Build prefix sums on the previous dp, then use upper_bound on the sorted previous list to count all values <= current.

</details>