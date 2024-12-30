[3405. Count the Number of Arrays with K Matching Adjacent Elements](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/)

`Hard`

You are given three integers n, m, k. A good array arr of size n is defined as follows:

Each element in arr is in the inclusive range [1, m].
Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
Return the number of good arrays that can be formed.

Since the answer may be very large, return it modulo 10^9 + 7.

```
Example 1:
Input: n = 3, m = 2, k = 1
Output: 4
Explanation:

There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
Hence, the answer is 4.

Example 2:
Input: n = 4, m = 2, k = 2
Output: 6
Explanation:

The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
Hence, the answer is 6.

Example 3:
Input: n = 5, m = 2, k = 0
Output: 2
Explanation:

The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
```

Constraints:

- 1 <= n <= 10^5
- 1 <= m <= 10^5
- 0 <= k <= n - 1

Accepted
2.6K
Submissions
7.9K
Acceptance Rate
32.6%

<details>
<summary>Hint 1</summary>

The first position `arr[0]` has `m` choices.

</details>
<details>
<summary>Hint 2</summary>

For each of the remaining n - 1 indices, 0 < i < n, select k positions from left to right and set arr[i] = arr[i - 1].

</details>
<details>
<summary>Hint 3</summary>

For all other indices, set arr[i] != arr[i - 1] with (m - 1) choices for each of the n - 1 - k positions.

</details>