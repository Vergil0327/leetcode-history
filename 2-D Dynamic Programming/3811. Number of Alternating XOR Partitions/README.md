[3811. Number of Alternating XOR Partitions](https://leetcode.com/problems/number-of-alternating-xor-partitions/)

`Medium`

You are given an integer array nums and two distinct integers target1 and target2.

A partition of nums splits it into one or more contiguous, non-empty blocks that cover the entire array without overlap.

A partition is valid if the bitwise XOR of elements in its blocks alternates between target1 and target2, starting with target1.

Formally, for blocks b1, b2, …:

XOR(b1) = target1
XOR(b2) = target2 (if it exists)
XOR(b3) = target1, and so on.
Return the number of valid partitions of nums, modulo $10^9 + 7$.

Note: A single block is valid if its XOR equals target1.

 

Example 1:
Input: nums = [2,3,1,4], target1 = 1, target2 = 5
Output: 1
Explanation:​​​​​​​

The XOR of [2, 3] is 1, which matches target1.
The XOR of the remaining block [1, 4] is 5, which matches target2.
This is the only valid alternating partition, so the answer is 1.

Example 2:
Input: nums = [1,0,0], target1 = 1, target2 = 0
Output: 3
Explanation:

​​​​​​​The XOR of [1, 0, 0] is 1, which matches target1.
The XOR of [1] and [0, 0] are 1 and 0, matching target1 and target2.
The XOR of [1, 0] and [0] are 1 and 0, matching target1 and target2.
Thus, the answer is 3.​​​​​​​

Example 3:
Input: nums = [7], target1 = 1, target2 = 7
Output: 0
Explanation:

The XOR of [7] is 7, which does not match target1, so no valid partition exists.
 

Constraints:

- 1 <= nums.length <= $10^5$
- 0 <= nums[i], target1, target2 <= $10^5$
- target1 != target2
 

Accepted
5,951/24.4K
Acceptance Rate
24.4%

<details>
<summary>Hint 1</summary>

Use dynamic programming.

</details>
<details>
<summary>Hint 2</summary>

Compute prefix XORs so the XOR of a block [l..r] can be obtained as pref[r] ^ pref[l - 1].

</details>
<details>
<summary>Hint 3</summary>

For each position, try ending a block whose XOR equals the expected target, and transition to the next state (alternating between target1 and target2).

</details>
<details>
<summary>Hint 4</summary>
Use a hash map or array indexed by prefix XOR values to efficiently count valid previous split points.

</details>