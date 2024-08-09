[2222. Number of Ways to Select Buildings](https://leetcode.com/problems/number-of-ways-to-select-buildings/)

`Medium`

You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

```
Example 1:
Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.

Example 2:
Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
``` 

Constraints:

- 3 <= s.length <= 10^5
- s[i] is either '0' or '1'.

Accepted
37.2K
Submissions
73.5K
Acceptance Rate
50.7%

<details>
<summary>Hint 1</summary>

There are only 2 valid patterns: ‘101’ and ‘010’. Think about how we can construct these 2 patterns from smaller patterns.

</details>
<details>
<summary>Hint 2</summary>

Count the number of subsequences of the form ‘01’ or ‘10’ first. Let n01[i] be the number of ‘01’ subsequences that exist in the prefix of s up to the ith building. How can you compute n01[i]?

</details>
<details>
<summary>Hint 3</summary>

Let n0[i] and n1[i] be the number of ‘0’s and ‘1’s that exists in the prefix of s up to i respectively. Then n01[i] = n01[i – 1] if s[i] == ‘0’, otherwise n01[i] = n01[i – 1] + n0[i – 1].

</details>
<details>
<summary>Hint 4</summary>

The same logic applies to building the n10 array and subsequently the n101 and n010 arrays for the number of ‘101’ and ‘010‘ subsequences.

</details>