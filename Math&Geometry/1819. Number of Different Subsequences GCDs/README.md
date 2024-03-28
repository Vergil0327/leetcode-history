[1819. Number of Different Subsequences GCDs](https://leetcode.com/problems/number-of-different-subsequences-gcds/)

`Hard`

You are given an array nums that consists of positive integers.

The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence evenly.

For example, the GCD of the sequence [4,6,16] is 2.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
Return the number of different GCDs among all non-empty subsequences of nums.

```
Example 1:
Input: nums = [6,10,3]
Output: 5
Explanation: The figure shows all the non-empty subsequences and their GCDs.
The different GCDs are 6, 10, 3, 2, and 1.

Example 2:
Input: nums = [5,15,40,5,6]
Output: 7
``` 

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 2 * 10^5

<details>
<summary>Hint 1</summary>

Think of how to check if a number x is a gcd of a subsequence.

</details>
<details>
<summary>Hint 2</summary>

If there is such subsequence, then all of it will be divisible by x. Moreover, if you divide each number in the subsequence by x , then the gcd of the resulting numbers will be 1.

</details>
<details>
<summary>Hint 3</summary>

Adding a number to a subsequence cannot increase its gcd. So, if there is a valid subsequence for x , then the subsequence that contains all multiples of x is a valid one too.

</details>
<details>
<summary>Hint 4</summary>

Iterate on all possible x from 1 to 10^5, and check if there is a valid subsequence for x.

</details>