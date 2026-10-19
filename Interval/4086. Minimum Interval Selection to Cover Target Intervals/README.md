[4086. Minimum Interval Selection to Cover Target Intervals](https://leetcode.com/problems/minimum-interval-selection-to-cover-target-intervals/)

`Hard`

You are given two 2D integer arrays, `availableIntervals` and `targetIntervals`, each representing a list of closed intervals.

Select a subset of intervals from availableIntervals so that every real point contained in any interval in targetIntervals belongs to at least one selected interval.

Points outside the target intervals do not need to be covered. Selected intervals may overlap or extend beyond the target intervals.

Return the minimum number of intervals you need to select. If it is impossible to cover all the target intervals, return -1.


Example 1:
Input: availableIntervals = [[1,4],[1,7],[3,9],[5,10],[10,15]], targetIntervals = [[1,3],[2,5],[7,8],[10,13],[11,15],[12,13]]
Output: 3
Explanation:

The target intervals cover the ranges [1, 5], [7, 8], and [10, 15]. By selecting [1, 4], [3, 9], and [10, 15] from availableIntervals, all target intervals can be fully covered with three intervals.

Example 2:
Input: availableIntervals = [[4,6],[1,4],[2,5]], targetIntervals = [[3,4],[2,5],[6,7]]
Output: -1
Explanation:
It is impossible to select intervals from availableIntervals to cover all the intervals in targetIntervals.

Example 3:
Input: availableIntervals = [[1,2],[3,4]], targetIntervals = [[1,4]]
Output: -1
Explanation:

Selecting both available intervals leaves every real point strictly between 2 and 3 uncovered. For example, 2.5 belongs to the target interval but to neither available interval.

Constraints:

- 1 <= availableIntervals.length, targetIntervals.length <= 5 * 10^4
- availableIntervals[i].length == targetIntervals[j].length == 2
- 1 <= availableIntervals[i][0] <= availableIntervals[i][1] <= 10^5
- 1 <= targetIntervals[j][0] <= targetIntervals[j][1] <= 10^5

Accepted
3,068/10K
Acceptance Rate
30.8%

<details>
<summary>Hint 1</summary>
1a (Sorting and Greedy): Sort both lists by left endpoint and merge overlapping target intervals. Intervals sharing an endpoint can be merged, but intervals separated by a positive gap cannot.
</details>
<details>
<summary>Hint 2</summary>
1b (Sorting and Greedy): At the start of an uncovered target interval, choose an available interval containing that point whose right endpoint is farthest.
</details>
<details>
<summary>Hint 3</summary>
1c (Sorting and Greedy): If coverage currently reaches x inside a target interval, the next selected interval must start at or before x and extend beyond it. Do not advance to x + 1, since every real point must be covered.
</details>
<details>
<summary>Hint 4</summary>
1d (Sorting and Greedy): Once a target interval is covered, move to the next target interval while retaining the coverage already obtained. Return -1 if a required point cannot be covered or coverage cannot be extended.
</details>
<details>
<summary>Hint 5</summary>
2a (Doubled-Coordinate Sweep): Map each interval [l, r] to the integer positions from 2 * l through 2 * r. These positions represent original integer coordinates and their midpoints, which suffice because all interval endpoints are integers.
</details>
<details>
<summary>Hint 6</summary>
2b (Doubled-Coordinate Sweep): Use a difference array to mark required positions. For each position, precompute the farthest right endpoint among available intervals starting at or before it.
</details>
<details>
<summary>Hint 7</summary>
2c (Doubled-Coordinate Sweep): Sweep from left to right. Whenever a required position is not covered, select the interval reaching farthest right that covers it. If none exists, return -1.
</details>