[2521. Distinct Prime Factors of Product of Array](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/)

`Medium`

Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.

Note that:

A number greater than 1 is called prime if it is divisible by only 1 and itself.
An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.
 
```
Example 1:
Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.

Example 2:
Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.
```

Constraints:

- 1 <= nums.length <= $10^4$
- 2 <= nums[i] <= 1000

<details>
<summary>Hint 1</summary>

Do not multiply all the numbers together, as the product is too big to store.

</details>

<details>
<summary>Hint 2</summary>

Think about how each individual number's prime factors contribute to the prime factors of the product of the entire array.

</details>

<details>
<summary>Hint 3</summary>

Find the prime factors of each element in nums, and store all of them in a set to avoid duplicates.

</details>