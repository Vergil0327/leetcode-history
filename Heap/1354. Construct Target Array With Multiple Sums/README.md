[1354. Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/description/)

`Hard`

You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < n and set the value of arr at index i to x.
You may repeat this procedure as many times as needed.
Return true if it is possible to construct the target array from arr, otherwise, return false.

```
Example 1:
Input: target = [9,3,5]
Output: true
Explanation: Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

Example 2:
Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].

Example 3:
Input: target = [8,5]
Output: true
``` 

Constraints:

- n == target.length
- 1 <= n <= 5 * 10^4
- 1 <= target[i] <= 10^9

Acceptance Rate
36.3%

<details>
<summary>Hint 1</summary>

Given that the sum is strictly increasing, the largest element in the target must be formed in the last step by adding the total sum in the previous step. Thus, we can simulate the process in a reversed way.

</details>

<details>
<summary>Hint 2</summary>

Subtract the largest with the rest of the array, and put the new element into the array. Repeat until all elements become one

</details>