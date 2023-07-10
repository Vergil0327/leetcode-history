[777. Swap Adjacent in LR String](https://leetcode.com/problems/swap-adjacent-in-lr-string/description/)

`Medium`

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

```
Example 1:
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:
Input: start = "X", end = "L"
Output: false
``` 

Constraints:

- 1 <= start.length <= 10^4
- start.length == end.length
- Both start and end will only consist of characters in 'L', 'R', and 'X'.

Acceptance Rate
36.8%

<details>
<summary>Hint</summary>

Think of the L and R's as people on a horizontal line, where X is a space. The people can't cross each other, and also you can't go from XRX to RXX.

</details>