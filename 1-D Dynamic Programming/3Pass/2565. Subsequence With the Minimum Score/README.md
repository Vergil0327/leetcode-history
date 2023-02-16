[2565. Subsequence With the Minimum Score](https://leetcode.com/problems/subsequence-with-the-minimum-score/description/)

`Hard`

You are given two strings s and t.

You are allowed to remove any number of characters from the string t.

The score string is 0 if no characters are removed from the string t, otherwise:

Let left be the minimum index among all removed characters.
Let right be the maximum index among all removed characters.
Then the score of the string is right - left + 1.

Return the minimum possible score to make t a subsequence of s.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

```
Example 1:
Input: s = "abacaba", t = "bzaa"
Output: 1
Explanation: In this example, we remove the character "z" at index 1 (0-indexed).
The string t becomes "baa" which is a subsequence of the string "abacaba" and the score is 1 - 1 + 1 = 1.
It can be proven that 1 is the minimum score that we can achieve.

Example 2:
Input: s = "cde", t = "xyz"
Output: 3
Explanation: In this example, we remove characters "x", "y" and "z" at indices 0, 1, and 2 (0-indexed).
The string t becomes "" which is a subsequence of the string "cde" and the score is 2 - 0 + 1 = 3.
It can be proven that 3 is the minimum score that we can achieve.
```

Constraints:

- 1 <= s.length, t.length <= 10^5
- s and t consist of only lowercase English letters.

<details>
<summary>Hint 1</summary>

Maintain two pointers: i and j. We need to perform a similar operation: while t[0:i] + t[j:n] is not a subsequence of the string s, increase j.

</details>

<details>
<summary>Hint 2</summary>

We can check the condition greedily. Create the array leftmost[i] which denotes minimum index k, such that in prefix s[0:k] exists subsequence t[0:i]. Similarly, we define rightmost[i].

</details>

<details>
<summary>Hint 3</summary>

If leftmost[i] < rightmost[j] then t[0:i] + t[j:n] is the subsequence of s.

</details>

<details>
<summary>Solution</summary>

@queetcode
```c++
class Solution {
public:
    int minimumScore(string s, string t) {
        vector<int> p; 
        int j = 0; 
        for (int i = 0; i < s.size(); ++i) {
            if (j < t.size() && s[i] == t[j]) ++j; 
            p.push_back(j); 
        }
        int ans = t.size() - j; 
        j = t.size()-1; 
        for (int i = s.size()-1; i >= 0; --i) {
            ans = min(ans, max(0, j - p[i] + 1)); 
            if (0 <= j && s[i] == t[j]) --j; 
        }
        return min(ans, j+1); 
    }
};
```
</details>