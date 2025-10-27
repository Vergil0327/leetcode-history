[3728. Stable Subarrays With Equal Boundary and Interior Sum](https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/)

`Medium`

You are given an integer array capacity.

A subarray capacity[l..r] is considered stable if:

- Its length is at least 3.
- The first and last elements are each equal to the sum of all elements strictly between them (i.e., capacity[l] = capacity[r] = capacity[l + 1] + capacity[l + 2] + ... + capacity[r - 1]).
Return an integer denoting the number of stable subarrays.

```
Example 1:
Input: capacity = [9,3,3,3,9]
Output: 2
Explanation:

[9,3,3,3,9] is stable because the first and last elements are both 9, and the sum of the elements strictly between them is 3 + 3 + 3 = 9.
[3,3,3] is stable because the first and last elements are both 3, and the sum of the elements strictly between them is 3.

Example 2:
Input: capacity = [1,2,3,4,5]
Output: 0
Explanation:

No subarray of length at least 3 has equal first and last elements, so the answer is 0.

Example 3:
Input: capacity = [-4,4,0,0,-8,-4]
Output: 1
Explanation:

[-4,4,0,0,-8,-4] is stable because the first and last elements are both -4, and the sum of the elements strictly between them is 4 + 0 + 0 + (-8) = -4
```

Constraints:

- 3 <= capacity.length <= $10^5$
- -10^9 <= capacity[i] <= 10^9

<details>
<summary>Hint 1</summary>

Use prefix sums

</details>
<details>
<summary>Hint 2</summary>

Let the prefix sum array be p; notice that for a stable range [l, r], the condition becomes p[r - 1] - p[l] == a[r] and a[l] == a[r]

</details>
<details>
<summary>Hint 3</summary>

For each index r, you want to count the number of previous indices l such that p[l] == p[r - 1] - a[r] and a[l] == a[r]

</details>
<details>
<summary>Hint 4</summary>

You can do this efficiently by maintaining a map from (a[i], p[i]) to a frequency count as you iterate

</details>