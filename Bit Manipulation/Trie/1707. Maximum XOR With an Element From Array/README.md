[1707. Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

`Hard`

You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.

```
Example 1:
Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
Explanation:
1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

Example 2:
Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
Output: [15,-1,5]
``` 

Constraints:

- 1 <= nums.length, queries.length <= 10^5
- queries[i].length == 2
- 0 <= nums[j], xi, mi <= 10^9

Accepted
19.6K
Submissions
40.3K
Acceptance Rate
48.6%

<details>
<summary>Hint 1</summary>

In problems involving bitwise operations, we often think on the bits level. In this problem, we can think that to maximize the result of an xor operation, we need to maximize the most significant bit, then the next one, and so on.

</details>
<details>
<summary>Hint 2</summary>

If there's some number in the array that is less than m and whose the most significant bit is different than that of x, then xoring with this number maximizes the most significant bit, so I know this bit in the answer is 1.

</details>
<details>
<summary>Hint 3</summary>

To check the existence of such numbers and narrow your scope for further bits based on your choice, you can use trie.

</details>
<details>
<summary>Hint 4</summary>

You can sort the array and the queries, and maintain the trie such that in each query the trie consists exactly of the valid elements.

</details>