[3485. Longest Common Prefix of K Strings After Removal](https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/)

`Hard`

You are given an array of strings words and an integer k.

For each index i in the range [0, words.length - 1], find the length of the longest common prefix among any k strings (selected at distinct indices) from the remaining array after removing the ith element.

Return an array answer, where answer[i] is the answer for ith element. If removing the ith element leaves the array with fewer than k strings, answer[i] is 0.

``` 
Example 1:
Input: words = ["jump","run","run","jump","run"], k = 2
Output: [3,4,4,3,4]
Explanation:

Removing index 0 ("jump"):
words becomes: ["run", "run", "jump", "run"]. "run" occurs 3 times. Choosing any two gives the longest common prefix "run" (length 3).
Removing index 1 ("run"):
words becomes: ["jump", "run", "jump", "run"]. "jump" occurs twice. Choosing these two gives the longest common prefix "jump" (length 4).
Removing index 2 ("run"):
words becomes: ["jump", "run", "jump", "run"]. "jump" occurs twice. Choosing these two gives the longest common prefix "jump" (length 4).
Removing index 3 ("jump"):
words becomes: ["jump", "run", "run", "run"]. "run" occurs 3 times. Choosing any two gives the longest common prefix "run" (length 3).
Removing index 4 ("run"):
words becomes: ["jump", "run", "run", "jump"]. "jump" occurs twice. Choosing these two gives the longest common prefix "jump" (length 4).

Example 2:
Input: words = ["dog","racer","car"], k = 2
Output: [0,0,0]
Explanation:
Removing any index results in an answer of 0.
```

Constraints:

- 1 <= k <= words.length <= 10^5
- 1 <= words[i].length <= 10^4
- words[i] consists of lowercase English letters.
- The sum of words[i].length is smaller than or equal 10^5.

Accepted
3K
Submissions
19.1K
Acceptance Rate
15.7%

<details>
<summary>Hint 1</summary>

Use a trie to store all the strings initially.

</details>
<details>
<summary>Hint 2</summary>

For each node in the trie, maintain the count of paths ending there.

</details>
<details>
<summary>Hint 3</summary>

For each `arr[i]`, remove it from the trie and update the counts.

</details>
<details>
<summary>Hint 4</summary>

During evaluation, find the innermost node with at least k paths ending there.

</details>
<details>
<summary>Hint 5</summary>

Use a multiset or similar structure to handle updates efficiently.

</details>