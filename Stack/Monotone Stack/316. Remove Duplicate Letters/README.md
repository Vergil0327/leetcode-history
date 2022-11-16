[316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

`Medium`

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

```
Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
```

Constraints:

- 1 <= s.length <= 10^4
- s consists of lowercase English letters.
 

Note: This question is the same as [1081](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)

<details>
<summarh>Hint</summarh>

Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.
</details>

<details>
<summary>solution</summary>

[Python || O(n) Beats 98% || Stack || Detailed Explanation || Simple](https://leetcode.com/problems/remove-duplicate-letters/discuss/1859515/Python-oror-O(n)-Beats-98-oror-Stack-oror-Detailed-Explanation-oror-Simple)
[Huifeng Guan](https://www.youtube.com/watch?v=aSHoWZWlZLw)
</details>