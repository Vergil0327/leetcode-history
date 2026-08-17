[4026. Maximum Gap Between Stations](https://leetcode.com/problems/maximum-gap-between-stations/)

`Medium`

You are given two strings skill and station of lengths n and m, respectively.

skill[i] represents the skill of worker i, and station[j] represents the skill supported by station j.

You must assign every worker to a distinct station. Let ji be the index of the station assigned to worker i. A valid assignment must satisfy:

- station[ji] == skill[i] for every 0 <= i < n.
- The assigned station indices must be strictly increasing in worker order, meaning j0 < j1 < ... < jn - 1.
- The gap of an assignment is the maximum difference between the station indices assigned to two consecutive workers. In other words, it is max(ji - ji - 1) over all 1 <= i < n.

If there is only one worker, the gap is 0.

Return the maximum possible gap among a ll valid assignments. It is guaranteed that at least one valid assignment exists.


Example 1:
Input: skill = "aa", station = "aaaa"
Output: 3
Explanation:

The two workers must be assigned to two different 'a' stations.
Assigning them to stations [0, 3] gives a gap of 3.

Example 2:
Input: skill = "xyz", station = "xyzz"
Output: 2
Explanation:

Assign worker 0 to station j = 0, and worker 1 to station j = 1.
To maximize the gap, assign worker 2 to station j = 3.
This gives the assignment [0, 1, 3] with gaps [1, 2], so the gap is 2.

Example 3:
Input: skill = "cbc", station = "cbcdbc"
Output: 4
Explanation:

Assign worker 0 to station j = 0, and worker 1 to station j = 1.
To maximize the gap, assign worker 2 to station j = 5.
This gives the assignment [0, 1, 5] with gaps [1, 4], so the gap is 4.
 

Constraints:

- skill.length == n
- station.length == m
- 1 <= n <= m <= 10^5
- skill and station consist of lowercase English letters.
- It is guaranteed that a valid assignment exists for every worker.

Accepted
17,629/33.1K
Acceptance Rate
53.2%


<details>
<summary>Hint 1</summary>
For each adjacent pair of workers i - 1 and i, try to maximize the distance between their assigned stations while still allowing all earlier and later workers to be matched.
</details>
<details>
<summary>Hint 2</summary>
Compute the earliest possible station index for every worker by greedily matching skill from left to right.
</details>
<details>
<summary>Hint 3</summary>
Compute the latest possible station index for every worker by greedily matching skill from right to left.
</details>
<details>
<summary>Hint 4</summary>
For each 1 <= i < n, workers before i can use their earliest possible positions and workers from i onward can use their latest possible positions. The largest possible gap between workers i - 1 and i is latest[i] - earliest[i - 1].
</details>