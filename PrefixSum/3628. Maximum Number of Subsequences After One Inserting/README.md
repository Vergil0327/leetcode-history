[3628. Maximum Number of Subsequences After One Inserting](https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/)

`Medium`

You are given a string s consisting of uppercase English letters.

You are allowed to insert at most one uppercase English letter at any position (including the beginning or end) of the string.

Return the maximum number of "LCT" subsequences that can be formed in the resulting string after at most one insertion.

```
Example 1:
Input: s = "LMCT"
Output: 2
Explanation:

We can insert a "L" at the beginning of the string s to make "LLMCT", which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].
```

Constraints:

- 1 <= s.length <= 10^5
- s consists of uppercase English letters.

Accepted
11,023/49.9K
Acceptance Rate
22.1%

<details>
<summary>Hint 1</summary>

Precompute preL, preLC, sufT, and sufCT arrays to count L’s, LC’s, T’s, and CT’s at each position.

</details>
<details>
<summary>Hint 2</summary>

Compute base as the sum over all i of preLC[i] * sufT[i].

</details>
<details>
<summary>Hint 3</summary>

For each insert position i, compute gains sufCT[i] for ‘L’, preL[i] * sufT[i] for ‘C’, and preLC[i] for ‘T’, and take the maximum of base and base + gain.

</details>