[4055. Count Shadow Pairs II](https://leetcode.com/problems/count-shadow-pairs-ii/)

`Hard`

You are given an integer array nums of length n.

A pair of indices (i, j) is called a shadow pair if all of the following conditions are satisfied:

- 0 <= i < j < n
- nums[i] < nums[j]
- There does not exist an index k such that i < k < j and nums[i] < nums[k] < nums[j].
Return the total number of shadow pairs.

Example 1:
Input: nums = [3,1,4,2,5]
Output: 5
Explanation:

(i, j)	nums[i]	nums[j]	Shadow Pair
(0, 2)	  3	      4	    nums[1] = 1 is not strictly between 3 and 4
(1, 2)	  1	      4	    No index k exists such that 1 < k < 2
(1, 3)	  1	      2	    nums[2] = 4 is not strictly between 1 and 2
(2, 4)	  4	      5	    nums[3] = 2 is not strictly between 4 and 5
(3, 4)	  2	      5	    No index k exists such that 3 < k < 4
Thus, the answer is 5.

Example 2:
Input: nums = [6,7,8,9]
Output: 3
Explanation:

(i, j)	nums[i]	nums[j]	Shadow Pair
(0, 1)	6	7	No index k exists such that 0 < k < 1
(1, 2)	7	8	No index k exists such that 1 < k < 2
(2, 3)	8	9	No index k exists such that 2 < k < 3
Thus, the answer is 3.

Constraints:

- 3 <= n == nums.length <= 5 * 10^4
- 1 <= nums[i] <= 10^9

Accepted
1,066/7.3K
Acceptance Rate
14.5%

<details>
<summary>Hint 1</summary>

Divide the array into two halves. Recursively count pairs within each half, then count pairs whose endpoints lie in different halves.

</details>
<details>
<summary>Hint 2</summary>

For each left endpoint i, let b[i] be the smallest value greater than nums[i] appearing after i in the left half, or positive infinity if none exists. For each right endpoint j, let c[j] be the largest value smaller than nums[j] appearing before j in the right half, or negative infinity if none exists. Compute these bounds using ordered sets.

</details>
<details>
<summary>Hint 3</summary>

A pair crossing the split is valid exactly when c[j] <= nums[i] < nums[j] <= b[i].

</details>
<details>
<summary>Hint 4</summary>

Process right endpoints in increasing order of nums[j]. Use a Fenwick tree over compressed values to maintain left endpoints satisfying nums[i] < nums[j] <= b[i], then count those with nums[i] >= c[j]. This gives an overall O(n log2 n) solution.

</details>