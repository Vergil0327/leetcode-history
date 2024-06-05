[745. Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/)

`Hard`

Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 
```
Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
```

Constraints:

- 1 <= words.length <= 10^4
- 1 <= words[i].length <= 7
- 1 <= pref.length, suff.length <= 7
- words[i], pref and suff consist of lowercase English letters only.
- At most 10^4 calls will be made to the function f.

Accepted
96.7K
Submissions
234.9K
Acceptance Rate
41.2%

<details>
<summary>Hint 1</summary>

Take "apple" as an example, we will insert add "apple{apple", "pple{apple", "ple{apple", "le{apple", "e{apple", "{apple" into the Trie Tree.

</details>
<details>
<summary>Hint 2</summary>

If the query is: prefix = "app", suffix = "le", we can find it by querying our trie for "le { app".

</details>
<details>
<summary>Hint 3</summary>

We use '{' because in ASCii Table, '{' is next to 'z', so we just need to create new TrieNode[27] instead of 26. Also, compared with traditional Trie, we add the attribute weight in class TrieNode. You can still choose any different character.

</details>