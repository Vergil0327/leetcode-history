[3863. Minimum Operations to Sort a String](https://leetcode.com/problems/minimum-operations-to-sort-a-string/)

`Medium`

You are given a string s consisting of lowercase English letters.

In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.

Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

 

Example 1:
Input: s = "dog"
Output: 1
Explanation:​​​​​​​

Sort substring "og" to "go".
Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.

Example 2:
Input: s = "card"
Output: 2
Explanation:

Sort substring "car" to "acr", so s = "acrd".
Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.

Example 3:
Input: s = "gf"
Output: -1

Explanation:

It is impossible to sort s under the given constraints. Thus, the answer is -1.
 

Constraints:

- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
 

Accepted
11,016/68.5K
Acceptance Rate
16.1%

<details>
<summary>Hint 1</summary>

If s is already sorted, answer is 0.

</details>
<details>
<summary>Hint 2</summary>

Let mn be the minimum char and mx be the maximum char; if mn appears at the beginning (not whole string) or mx appears at the end (not whole string), answer is 1.

</details>
<details>
<summary>Hint 3</summary>

If s cannot be transformed into a sorted string, return -1.

</details>
<details>
<summary>Hint 4</summary>

If no mn exists in any proper prefix and no mx exists in any proper suffix, answer is 3; otherwise answer is 2

</details>