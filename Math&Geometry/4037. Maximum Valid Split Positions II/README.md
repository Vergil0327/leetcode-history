[4037. Maximum Valid Split Positions II](https://leetcode.com/problems/maximum-valid-split-positions-ii/)

`Hard`

You are given an integer array nums.

You may remove at most one element from nums. Let arr be the array of remaining elements in their original order, and let m be its length.

A split position i of arr is valid if:

- 0 <= i < m - 1, and
- gcd(arr[0..i]) == gcd(arr[i + 1..m - 1]).
An array of length 1 has no valid split positions.

The score of arr is the number of valid split positions in it.
Return the maximum possible score of arr.

Here, gcd(a) denotes the greatest common divisor of all elements in the array a.


Example 1:
Input: nums = [10,30,15,10]
Output: 2
Explanation:

One optimal solution is to remove nums[2] = 15. Then arr = [10, 30, 10].

The split positions are:

Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
0	10	10
1	10	10
All split positions are valid. Thus, the answer is 2.

Example 2:
Input: nums = [2,10,14]
Output: 1
Explanation:
One optimal solution is to not remove any element. Then arr = [2, 10, 14].

The split positions are:

Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
0	2	2
1	2	14
Only the split position at index 0 is valid. Thus, the answer is 1.

Example 3:
Input: nums = [2,4]
Output: 0
Explanation:
The only remaining array that has a split position is arr = [2, 4].

The split positions are:

Split Position i	gcd(arr[0..i])	gcd(arr[i + 1..m - 1])
0	2	4
There are no valid split positions. Thus, the answer is 0.

Constraints:

- 2 <= nums.length <= $10^5$
- 1 <= nums[i] <= $10^9​​​​$

Accepted
2,259/8K
Acceptance Rate
28.1%

<details>
<summary>
Hint 1
</summary>

Precompute prefix and suffix GCDs, and also consider the case where no element is removed. For a fixed removed index j, splits entirely to either side of j can be expressed using the GCD of two unaffected ranges; if 0 < j < n - 1, also consider the new split created between nums[j - 1] and nums[j + 1].
</details>

<details>
<summary>
Hint 2
</summary>

Do not examine every split separately for every j. As one endpoint of a range moves, its GCD can change only a small number of times: every strict decrease changes it to a proper divisor. Group consecutive split positions having the same GCD and process those groups together.
</details>