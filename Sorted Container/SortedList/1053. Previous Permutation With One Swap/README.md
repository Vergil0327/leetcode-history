[1053. Previous Permutation With One Swap](https://leetcode.com/problems/previous-permutation-with-one-swap/)

`Medium`

Given an array of positive integers arr (not necessarily distinct), return the 
lexicographically
 largest permutation that is smaller than arr, that can be made with exactly one swap. If it cannot be done, then return the same array.

Note that a swap exchanges the positions of two numbers arr[i] and arr[j]

```
Example 1:
Input: arr = [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.

Example 2:
Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.

Example 3:
Input: arr = [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
``` 

Constraints:

- 1 <= arr.length <= 10^4
- 1 <= arr[i] <= 10^4

Accepted
42.9K
Submissions
86.6K
Acceptance Rate
49.5%

<details>
<summary>Hint 1</summary>

You need to swap two values, one larger than the other. Where is the larger one located?

</details>