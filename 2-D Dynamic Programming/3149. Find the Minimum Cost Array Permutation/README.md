[3149. Find the Minimum Cost Array Permutation](https://leetcode.com/problems/find-the-minimum-cost-array-permutation/)

`Hard`

You are given an array nums which is a  permutation of [0, 1, 2, ..., n - 1]. The score of any permutation of [0, 1, 2, ..., n - 1] named perm is defined as:

> score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|

Return the permutation perm which has the minimum possible score. If multiple permutations exist with this score, return the one that is 
lexicographically smallest
 among them.

Example 1:
Input: nums = [1,0,2]
Output: [0,1,2]

![img](https://assets.leetcode.com/uploads/2024/04/04/example0gif.gif)

Explanation:
The lexicographically smallest permutation with minimum cost is [0,1,2]. The cost of this permutation is |0 - 0| + |1 - 2| + |2 - 1| = 2.

Example 2:
Input: nums = [0,2,1]
Output: [0,2,1]

![img2](https://assets.leetcode.com/uploads/2024/04/04/example1gif.gif)

Explanation:
The lexicographically smallest permutation with minimum cost is [0,2,1]. The cost of this permutation is |0 - 1| + |2 - 2| + |1 - 0| = 2.

Constraints:

- 2 <= n == nums.length <= 14
- nums is a permutation of [0, 1, 2, ..., n - 1].

Accepted
1.7K
Submissions
9.9K
Acceptance Rate
17.4%


<details>
<summary>Hint 1</summary>

The score function is cyclic, so we can always set perm[0] = 0 for the smallest lexical order.

</details>
<details>
<summary>Hint 2</summary>

It’s similar to the Traveling Salesman Problem. Use Dynamic Programming.

</details>
<details>
<summary>Hint 3</summary>

Use a bitmask to track which elements have been assigned to perm.

</details>