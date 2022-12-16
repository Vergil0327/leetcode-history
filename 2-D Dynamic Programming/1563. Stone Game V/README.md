[1563. Stone Game V](https://leetcode.com/problems/stone-game-v/description/)

`Hard`

There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's is initially zero.

Return the maximum score that Alice can obtain.

```
Example 1:
Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

Example 2:
Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28

Example 3:
Input: stoneValue = [4]
Output: 0
```

Constraints:

- 1 <= stoneValue.length <= 500
- 1 <= stoneValue[i] <= 10^6

<details>
<summary>Solution (N^3, TLE)</summary>

[huifengGuan](https://www.youtube.com/watch?v=2_JkASlmxTA)
</details>

<details>
<summary>Solution</summary>

time: O(n^2)

```python
'''
Suppose we know the k' for stones[i..j], what do we know about k' for stones[i..j+1]? It is either the same or it got shifted a few places to the right.
And so if we calculate dp values in the order: dp[i][i], dp[i][i+1], dp[i][i+2], ..., dp[i][j], we can essentially keep track of k' as we go within that same linear time bound.

Using this idea, we implement the final solution. Couple of pointers about my code:

1) mid: represents k' or first index such that left half >= right half
2) with i < j, max[i][j] represents left[i][j] of previous solution i.e. max(dp[i][i], dp[i][i+1], dp[i][i+2] .. dp[i][j]) and max[j][i] represents right[i][j] of previous solution i.e. max(dp[i][j], dp[i+1][j], dp[i+2][j] .. dp[j][j]). We could have used two different arrays left and right just like previous solution but this trick saves space.
3) I am traversing in the order: dp[j][j], dp[j-1,j], dp[j-2, j], .., dp[i][j] instead of the above mentioned order but the idea remains same.
'''

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        sz = len(stoneValue)
        dp, maxScore = [[0] * sz for _ in range(sz)], [[0] * sz for _ in range(sz)]
        for i in range(sz):
            maxScore[i][i] = stoneValue[i]
        for j in range(1, sz):
            mid, sm, rightHalf = j, stoneValue[j], 0
            for i in range(j - 1, -1, -1):
                sm += stoneValue[i]
                while (rightHalf + stoneValue[mid]) * 2 <= sm:
                    rightHalf += stoneValue[mid]
                    mid -= 1
                dp[i][j] = maxScore[i][mid] if rightHalf * 2 == sm else (0 if mid == i else maxScore[i][mid - 1]);
                dp[i][j] = max(dp[i][j], 0 if mid == j else maxScore[j][mid + 1])
                maxScore[i][j] = max(maxScore[i][j - 1], dp[i][j] + sm);
                maxScore[j][i] = max(maxScore[j][i + 1], dp[i][j] + sm);
        return dp[0][sz - 1]
```
</details>