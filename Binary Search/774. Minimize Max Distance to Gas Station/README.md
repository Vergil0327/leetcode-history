[774. Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/)

`Medium`

*SUBSCRIBE TO UNLOCK*

On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.

Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of D.

```
Example 1:
Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
Explanation: the distance between adjacent gas stations is 0.5

Example 2:
Input：stations = [3,6,12,19,33,44,67,72,89,95]，K = 2
Output：14.00
Explanation：Build gas station at 86

Example 3:
Input:[10, 19, 25, 27, 56, 63, 70, 87, 96, 97]，K = 3
Output: 9.67
Explanation: D between each i and i+1 are `[9，6，2，29，7，7，17，9，1]`
split 29 into three pieces, each piece is 9.67,
and split 17 into 2 pieces, each piece is 8.5
```

Note:

- stations.length will be an integer in range [10, 2000].
- stations[i] will be an integer in range [0, 10^8].
- K will be an integer in range [1, 10^6].
- Answers within 10^-6 of the true value will be accepted as correct.