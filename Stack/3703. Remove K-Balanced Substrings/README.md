[3703. Remove K-Balanced Substrings](https://leetcode.com/problems/remove-k-balanced-substrings/)

`Medium`

You are given a string s consisting of '(' and ')', and an integer k.

A string is k-balanced if it is exactly k consecutive '(' followed by k consecutive ')', i.e., '(' * k + ')' * k.

For example, if k = 3, k-balanced is "((()))".

You must repeatedly remove all non-overlapping k-balanced substrings from s, and then join the remaining parts. Continue this process until no k-balanced substring exists.

Return the final string after all possible removals.

```
​​​​​​​Example 1:
Input: s = "(())", k = 1
Output: ""
Explanation:
k-balanced substring is "()"

Step	Current s	k-balanced	Result s
1	(())	(())	()
2	()	()	Empty
Thus, the final string is "".

Example 2:
Input: s = "(()(", k = 1
Output: "(("
Explanation:
k-balanced substring is "()"

Step	Current s	k-balanced	Result s
1	(()(	(()(	((
2	((	-	((
Thus, the final string is "((".

Example 3:
Input: s = "((()))()()()", k = 3
Output: "()()()"
Explanation:
k-balanced substring is "((()))"

Step	Current s	k-balanced	Result s
1	((()))()()()	((()))()()()	()()()
2	()()()	-	()()()
Thus, the final string is "()()()".
```

Constraints:

- 2 <= s.length <= 10^5
- s consists only of '(' and ')'.
- 1 <= k <= s.length / 2
 

Accepted
13,668/44.7K
Acceptance Rate
30.6%

<details>
<summary>
Hint 1
</summary>
Use a stack
</details>
<details>
<summary>
Hint 2
</summary>
Try run-length encoding; operations only happen at boundaries of '(' and ')' runs
</details>
<details>
<summary>
Hint 3
</summary>
When adjacent runs are '(' then ')', you can cancel in blocks of k
</details>