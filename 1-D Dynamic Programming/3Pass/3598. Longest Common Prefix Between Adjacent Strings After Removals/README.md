[3598. Longest Common Prefix Between Adjacent Strings After Removals](https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/)

`Medium`

You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following steps:

Remove the element at index i from the words array.
Compute the length of the longest common prefix among all adjacent pairs in the modified array.
Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.

```
Example 1:
Input: words = ["jump","run","run","jump","run"]
Output: [3,0,0,3,3]
Explanation:

Removing index 0:
words becomes ["run", "run", "jump", "run"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
Removing index 1:
words becomes ["jump", "run", "jump", "run"]
No adjacent pairs share a common prefix (length 0)
Removing index 2:
words becomes ["jump", "run", "jump", "run"]
No adjacent pairs share a common prefix (length 0)
Removing index 3:
words becomes ["jump", "run", "run", "run"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
Removing index 4:
words becomes ["jump", "run", "run", "jump"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)

Example 2:
Input: words = ["dog","racer","car"]
Output: [0,0,0]
Explanation:

Removing any index results in an answer of 0.
```

Constraints:

- 1 <= words.length <= 10^5
- 1 <= words[i].length <= 10^4
- words[i] consists of lowercase English letters.
- The sum of words[i].length is smaller than or equal 105.

Accepted
12,551/42.1K
Acceptance Rate
29.8%

<details>
<summary>Hint 1</summary>

Precompute the longest common prefix length for adjacent prefixes and suffixes.

</details>
<details>
<summary>Hint 2</summary>

After deleting words[i], compute the longest common prefix for words[i - 1] and words[i + 1] (if they exist).

</details>
<details>
<summary>Hint 3</summary>

Use the result of the prefix computation up to i - 1 and the suffix computation from i + 1 onwards.

</details>