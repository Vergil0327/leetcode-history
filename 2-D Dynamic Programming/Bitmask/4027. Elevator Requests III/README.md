[4027. Elevator Requests III](https://leetcode.com/problems/elevator-requests-iii/)

`Hard`

You are given an integer n denoting the number of floors in a building, where the floors are numbered from 0 to n - 1.

You are also given an integer start and a 2D integer array requests, where requests[i] = [arrivali, floori] indicates that a request for floori is made at time arrivali.

At time 0, the elevator is at floor start.

At each second, the elevator may move up by 1 floor, move down by 1 floor, or remain on its current floor.

A request can be fulfilled only at or after its arrival time; it is fulfilled instantly when the elevator is on its requested floor at any time from its arrival time onward.

Return the minimum time needed to fulfill all requests.

Example 1:
Input: n = 9, start = 0, requests = [[0,8],[6,5]]
Output: 9
Explanation:

Move from floor 0 (start) to floor 5 (requests[1][1]) in 5 seconds, reaching at time 5. Since requests[1][0] = 6, wait until time 6 to fulfill it.
Move from floor 5 to floor 8 (requests[0][1]) in 3 seconds, fulfilling it at time 9.
Thus, all requests are fulfilled by time 9.

Example 2:
Input: n = 8, start = 5, requests = [[1,7],[7,3]]
Output: 7
Explanation:
Move from floor 5 (start) to floor 7 (requests[0][1]) in 2 seconds, reaching at time 2. Since requests[0][0] = 1 has already passed, floor 7 is fulfilled at time 2.
Move from floor 7 to floor 3 (requests[1][1]) in 4 seconds, reaching at time 6. Since requests[1][0] = 7, wait until time 7.
Thus, all requests are fulfilled by time 7.

Example 3:
Input: n = 7, start = 3, requests = [[0,5],[0,1],[6,3]]
Output: 8
Explanation:

Move from floor 3 (start) to floor 5 (requests[0][1]) in 2 seconds, fulfilling it at time 2.
Move from floor 5 to floor 1 (requests[1][1]) in 4 seconds, fulfilling it at time 6.
Move from floor 1 to floor 3 (requests[2][1]) in 2 seconds, reaching at time 8. Its request arrived at requests[2][0] = 6, so floor 3 is fulfilled at time 8.
Thus, all requests are fulfilled by time 8.

Constraints:

- 1 <= n <= 10^9
- 1 <= requests.length <= 16
- requests[i] == [arrivali, floori]
- 0 <= arrivali <= 10^9
- 0 <= start, floori <= n - 1

Accepted
4,051/9.8K
Acceptance Rate
41.4%


<details>
<summary>Hint 1</summary>
Since there are at most 16 requests, use bitmask dynamic programming over the set of requests already fulfilled.
</details>
<details>
<summary>Hint 2</summary>
Let dp[mask][i] be the minimum time at which all requests in mask can be fulfilled with request i being the last one visited.
</details>
<details>
<summary>Hint 3</summary>
If the elevator is at floor[i] at time t and next serves request j, the earliest time it can fulfill j is max(t + abs(floor[i] - floor[j]), arrival[j]).
</details>
<details>
<summary>Hint 4</summary>
Initialize each single-request state similarly using the distance from start, then take the minimum over all states containing every request.
</details>
