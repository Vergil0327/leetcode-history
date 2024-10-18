[1734. Decode XORed Permutation](https://leetcode.com/problems/decode-xored-permutation/)

`Medium`

There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.

```
Example 1:
Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]

Example 2:
Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]
``` 

Constraints:

- 3 <= n < 10^5
- n is odd.
- encoded.length == n - 1

Accepted
16.6K
Submissions
25.3K
Acceptance Rate
65.5%

<details>
<summary>Hint 1</summary>

Compute the XOR of the numbers between 1 and n, and think about how it can be used. Let it be x.

</details>
<details>
<summary>Hint 2</summary>

Think why n is odd.

</details>
<details>
<summary>Hint 3</summary>

perm[0] = x XOR encoded[1] XOR encoded[3] XOR encoded[5] ...

</details>
<details>
<summary>Hint 4</summary>

perm[i] = perm[i-1] XOR encoded[i-1]

</details>