[1499. Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/)

`Hard`

You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

```
Example 1:
Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.

Example 2:
Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
``` 

Constraints:

- 2 <= points.length <= 10^5
- points[i].length == 2
- -10^8 <= xi, yi <= 10^8
- 0 <= k <= 2 * 10^8
- xi < xj for all 1 <= i < j <= points.length
- xi form a strictly increasing sequence.

<details>
<summary>Hint 1</summary>

Use a priority queue to store for each point i, the tuple [yi-xi, xi]

</details>
<details>
<summary>Hint 2</summary>

Loop through the array and pop elements from the heap if the condition xj - xi > k, where j is the current index and i is the point on top the queue.

</details>
<details>
<summary>Hint 3</summary>

After popping elements from the queue. If the queue is not empty, calculate the equation with the current point and the point on top of the queue and maximize the answer.

</details>