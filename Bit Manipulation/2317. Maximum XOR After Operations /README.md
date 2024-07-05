[2317. Maximum XOR After Operations](https://leetcode.com/problems/maximum-xor-after-operations/)

`Medium`

You are given a 0-indexed integer array nums. In one operation, select any non-negative integer x and an index i, then update nums[i] to be equal to nums[i] AND (nums[i] XOR x).

Note that AND is the bitwise AND operation and XOR is the bitwise XOR operation.

Return the maximum possible bitwise XOR of all elements of nums after applying the operation any number of times.

```
Example 1:
Input: nums = [3,2,4,6]
Output: 7
Explanation: Apply the operation with x = 4 and i = 3, num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2.
Now, nums = [3, 2, 4, 2] and the bitwise XOR of all the elements = 3 XOR 2 XOR 4 XOR 2 = 7.
It can be shown that 7 is the maximum possible bitwise XOR.
Note that other operations may be used to achieve a bitwise XOR of 7.

Example 2:
Input: nums = [1,2,3,9,2]
Output: 11
Explanation: Apply the operation zero times.
The bitwise XOR of all the elements = 1 XOR 2 XOR 3 XOR 9 XOR 2 = 11.
It can be shown that 11 is the maximum possible bitwise XOR.
``` 

Constraints:

- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^8

Accepted
25.2K
Submissions
31.6K
Acceptance Rate
79.5%

<details>
<summary>Hint 1</summary>

Consider what it means to be able to choose any x for the operation and which integers could be obtained from a given nums[i].

</details>
<details>
<summary>Hint 2</summary>

The given operation can unset any bit in nums[i].

</details>
<details>
<summary>Hint 3</summary>

The nth bit of the XOR of all the elements is 1 if the nth bit is 1 for an odd number of elements. When can we ensure it is odd?

</details>
<details>
<summary>Hint 4</summary>

Try to set every bit of the result to 1 if possible.

</details>