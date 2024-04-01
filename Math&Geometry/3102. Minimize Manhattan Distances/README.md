[3102. Minimize Manhattan Distances](https://leetcode.com/problems/minimize-manhattan-distances/)

`Hard`

You are given a 0-indexed array points representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

The distance between two points is defined as their **Manhattan distance**.

> The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

Return the minimum possible value for maximum distance between any two points by removing exactly one point.

```
Example 1:
Input: points = [[3,10],[5,15],[10,2],[4,4]]
Output: 12
Explanation: The maximum distance after removing each point is the following:
- After removing the 0th point the maximum distance is between points (5, 15) and (10, 2), which is |5 - 10| + |15 - 2| = 18.
- After removing the 1st point the maximum distance is between points (3, 10) and (10, 2), which is |3 - 10| + |10 - 2| = 15.
- After removing the 2nd point the maximum distance is between points (5, 15) and (4, 4), which is |5 - 4| + |15 - 4| = 12.
- After removing the 3rd point the maximum distance is between points (5, 15) and (10, 2), which is |5 - 10| + |15 - 2| = 18.
It can be seen that 12 is the minimum possible maximum distance between any two points after removing exactly one point.

Example 2:
Input: points = [[1,1],[1,1],[1,1]]
Output: 0
Explanation: It can be seen that removing any of the points results in the maximum distance between any two points of 0.
``` 

Constraints:

- 3 <= points.length <= 10^5
- points[i].length == 2
- 1 <= points[i][0], points[i][1] <= 10^8

<details>
<summary>Hint 1</summary>

Notice that the Manhattan distance between two points [xi, yi] and [xj, yj] is  max({xi - xj + yi - yj, xi - xj - yi + yj, - xi + xj + yi - yj, - xi + xj - yi + yj}).

</details>
<details>
<summary>Hint 2</summary>

If you replace points as [xi - yi, xi + yi] then the Manhattan distance is max(max(xi) - min(xi), max(yi) - min(yi)) over all i.

</details>
<details>
<summary>Hint 3</summary>

After those observations, the problem just becomes a simulation. Create multiset of points [xi - yi, xi + yi], you can iterate on a point you might remove and get the maximum Manhattan distance over all other points.

</details>