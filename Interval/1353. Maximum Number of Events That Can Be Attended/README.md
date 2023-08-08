[1353. Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)

`Medium`

You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

```
Example 1:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
``` 

Constraints:

- 1 <= events.length <= 10^5
- events[i].length == 2
- 1 <= startDayi <= endDayi <= 10^5

Acceptance Rate
32.2%

<details>
<summary>Hint 1</summary>

Sort the events by the start time and in case of tie by the end time in ascending order.

</details>

<details>
<summary>Hint 2</summary>

Loop over the sorted events. Attend as much as you can and keep the last day occupied. When you try to attend new event keep in mind the first day you can attend a new event in.

</details>