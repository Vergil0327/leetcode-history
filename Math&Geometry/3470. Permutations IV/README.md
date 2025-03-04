[3470. Permutations IV](https://leetcode.com/problems/permutations-iv/)

`Hard`

Given two integers, n and k, an alternating permutation is a permutation of the first n positive integers such that no two adjacent elements are both odd or both even.

Return the k-th alternating permutation sorted in lexicographical order. If there are fewer than k valid alternating permutations, return an empty list.

```
Example 1:
Input: n = 4, k = 6
Output: [3,4,1,2]
Explanation:
The lexicographically-sorted alternating permutations of [1, 2, 3, 4] are:

[1, 2, 3, 4]
[1, 4, 3, 2]
[2, 1, 4, 3]
[2, 3, 4, 1]
[3, 2, 1, 4]
[3, 4, 1, 2] ← 6th permutation
[4, 1, 2, 3]
[4, 3, 2, 1]
Since k = 6, we return [3, 4, 1, 2].

Example 2:
Input: n = 3, k = 2
Output: [3,2,1]
Explanation:
The lexicographically-sorted alternating permutations of [1, 2, 3] are:

[1, 2, 3]
[3, 2, 1] ← 2nd permutation
Since k = 2, we return [3, 2, 1].

Example 3:
Input: n = 2, k = 3
Output: []
Explanation:

The lexicographically-sorted alternating permutations of [1, 2] are:

[1, 2]
[2, 1]
There are only 2 alternating permutations, but k = 3, which is out of range. Thus, we return an empty list [].
```

Constraints:

- 1 <= n <= 100
- 1 <= k <= 10^15

Accepted
1.5K
Submissions
7.1K
Acceptance Rate
21.5%

<details>
<summary>Hint 1</summary>

If n is odd, the first number must be odd.

</details>
<details>
<summary>Hint 2</summary>

If n is even, the first number can be either odd or even.

</details>
<details>
<summary>Hint 3</summary>

From smallest to largest, place each number and subtract the number of permutations from k.

</details>
<details>
<summary>Hint 4</summary>

The number of permutations can be calculated using factorials.

</details>