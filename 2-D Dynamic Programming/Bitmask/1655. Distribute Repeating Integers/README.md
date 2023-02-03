[1655. Distribute Repeating Integers](https://leetcode.com/problems/distribute-repeating-integers/description/)

`Hard`

You are given an array of n integers, nums, where there are at most 50 unique values in the array. You are also given an array of m customer order quantities, quantity, where quantity[i] is the amount of integers the ith customer ordered. Determine if it is possible to distribute nums such that:

The ith customer gets exactly quantity[i] integers,
The integers the ith customer gets are all equal, and
Every customer is satisfied.
Return true if it is possible to distribute nums according to the above conditions.

```
Example 1:
Input: nums = [1,2,3,4], quantity = [2]
Output: false
Explanation: The 0th customer cannot be given two different integers.

Example 2:
Input: nums = [1,2,3,3], quantity = [2]
Output: true
Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.

Example 3:
Input: nums = [1,1,2,2], quantity = [2,2]
Output: true
Explanation: The 0th customer is given [1,1], and the 1st customer is given [2,2].
```

Constraints:

- n == nums.length
- 1 <= n <= $10^5$
- 1 <= nums[i] <= 1000
- m == quantity.length
- 1 <= m <= 10
- 1 <= quantity[i] <= $10^5$
- There are at most 50 unique values in nums.

<details>
<summary>Solution</summary>

[HuifengGuan](https://www.youtube.com/watch?v=QExAjpLz20M)
[O(50*3^m) bitmask DP](https://leetcode.com/problems/distribute-repeating-integers/solutions/935554/python-3-o-50-3-m-bitmask-dp/)
</details>

<details>
<summary>Further Reading</summary>

[enumerate all submask](https://cp-algorithms.com/algebra/all-submasks.html)
</details>