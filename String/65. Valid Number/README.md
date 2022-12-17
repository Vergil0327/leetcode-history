[65. Valid Number](https://leetcode.com/problems/valid-number/description/)

`Hard`

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

```
Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false
```

Constraints:

- 1 <= s.length <= 20
- s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

<details>
<summary>Hint</summary>

check if "e" or "E" exists first.
if not exist, check if it is integer
if exist, break two parts and check if both is valid integer
</details>

<details>
<summary>Solution 1</summary>

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        e = dot = digit = False

        for i, c in enumerate(s):
            if c.isdigit():
                digit = True

            elif c in '+-':
                if i > 0 and s[i-1] not in 'Ee':
                    return False

            elif c in 'Ee':
                if e or not digit:
                    return False
                e = True
                digit = False
            elif c == '.':
                if dot or e:
                    return False
                dot = True
            else:
                return False
        return digit
```
</details>

<details>
<summary>Solution 2</summary>

[HuifengGuan](https://www.youtube.com/watch?v=REIQXR5p2Uo)
</details>