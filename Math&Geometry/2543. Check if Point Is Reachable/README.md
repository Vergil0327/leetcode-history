[2543. Check if Point Is Reachable](https://leetcode.com/problems/check-if-point-is-reachable/description/)

`Hard`

There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point (targetX, targetY) using a finite number of steps.

In one step, you can move from point (x, y) to any one of the following points:

(x, y - x)
(x - y, y)
(2 * x, y)
(x, 2 * y)
Given two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, return true if you can reach the point from (1, 1) using some number of steps, and false otherwise.

 

Example 1:

Input: targetX = 6, targetY = 9
Output: false
Explanation: It is impossible to reach (6,9) from (1,1) using any sequence of moves, so false is returned.
Example 2:

Input: targetX = 4, targetY = 7
Output: true
Explanation: You can follow the path (1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7).
 

Constraints:

1 <= targetX, targetY <= 10^9

<details>
<summary>Hint 1</summary>

Let’s go in reverse order, from (targetX, targetY) to (1, 1). So, now we can move from (x, y) to (x+y, y), (x, y+x), (x/2, y) if x is even, and (x, y/2) if y is even.

</details>

<details>
<summary>Hint 2</summary>

When is it optimal to use the third and fourth operations?

</details>

<details>
<summary>Hint 3</summary>

Think how GCD of (x, y) is affected if we apply the first two operations.

</details>

<details>
<summary>Hint 4</summary>

How can we check if we can reach (1, 1) using the GCD value calculate above?

</details>

<details>
<summary>Solution</summary>

[Huifeng](https://www.youtube.com/watch?v=6kCqGqYwWQU)

[Lee215](https://leetcode.com/problems/check-if-point-is-reachable/solutions/3082073/java-c-python-1-line-gcd-solution/)
[votrubac - Greedy vs. GCD](https://leetcode.com/problems/check-if-point-is-reachable/solutions/3082680/greedy-vs-gcd/?orderBy=most_votes)
[rock](https://leetcode.com/problems/check-if-point-is-reachable/solutions/3082013/java-python-3-check-if-the-gcd-has-only-factor-2-w-explanation-and-analysis/)


</details>