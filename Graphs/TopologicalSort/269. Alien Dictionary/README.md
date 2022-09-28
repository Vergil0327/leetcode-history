[269. Alien Dictionary](https://www.lintcode.com/problem/892/)

`hard`

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

```
Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Output: "wertf"

Explanation:
from "wrt" and "wrf", we can tell that 't'<'f'
from "wrt" and "er", we can tell that 'w'<'e'
from "er" and "ett", we can tell that 'r'<'t'
from "ett" and "rftt", we can tell that 'e'<'r'

Example 2:
Input:
[
  "z",
  "x"
]
Output: "zx"

Example 3:
Input:
[
  "z",
  "x",
  "z"
]
Output: "" 

Explanation: The order is invalid, so return "".
```

Note:

- You may assume all letters are in lowercase.
- You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
- If the order is invalid, return an empty string.
- There may be multiple valid order of letters, return any one of them is fine.