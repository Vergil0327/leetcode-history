[2478. Number of Beautiful Partitions](https://leetcode.com/problems/number-of-beautiful-partitions/)

`Hard`

You are given a string s that consists of the digits '1' to '9' and two integers k and minLength.

A partition of s is called beautiful if:

s is partitioned into k non-intersecting substrings.
Each substring has a length of at least minLength.
Each substring starts with a prime digit and ends with a non-prime digit. Prime digits are '2', '3', '5', and '7', and the rest of the digits are non-prime.
Return the number of beautiful partitions of s. Since the answer may be very large, return it modulo 109 + 7.

A substring is a contiguous sequence of characters within a string.

```
Example 1:
Input: s = "23542185131", k = 3, minLength = 2
Output: 3
"2354 | 218 | 5131"
"2354 | 21851 | 31"
Explanation: There exists three ways to create a beautiful partition:
"2354218 | 51 | 31"

Example 2:
Input: s = "23542185131", k = 3, minLength = 3
Output: 1
Explanation: There exists one way to create a beautiful partition: "2354 | 218 | 5131".

Example 3:
Input: s = "3312958", k = 3, minLength = 1
Output: 1
Explanation: There exists one way to create a beautiful partition: "331 | 29 | 58".
```

Constraints:

- 1 <= k, minLength <= s.length <= 1000
- s consists of the digits '1' to '9'.

<details>
<summary>Hint 1</summary>

For every index with composite value and every possible size of a partition, try to count the number of possible beautiful partitions.
</details>

<details>
<summary>Hint 2</summary>

Try to come up with O(n^2*k) dynamic programming solution.
</details>

<details>
<summary>Hint 3</summary>

To improve time complexity, one should notice that we can use two pointers to find the closest index with a prime value that is at least minLength away.
</details>

<details>
<summary>Hint 4</summary>

With prefix sum, we can maintain the sum of every possible beautiful partition before that index.
</details>
