[1291. Sequential Digits](https://leetcode.com/problems/sequential-digits)

`Medium`

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

```
Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
``` 

Constraints:

- 10 <= low <= high <= 10^9

Accepted
97.5K
Submissions
157.9K
Acceptance Rate
61.7%

<details>
<summary>Hint 1</summary>

Generate all numbers with sequential digits and check if they are in the given range.

</details>
<details>
<summary>Hint 2</summary>

Fix the starting digit then do a recursion that tries to append all valid digits.

</details>