[1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/description/)
`Medium`

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

```
Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:
Input: intervals = [[1,4],[2,3]]
Output: 1
```

Constraints:

- 1 <= intervals.length <= 1000
- intervals[i].length == 2
- 0 <= li < ri <= 10^5
- All the given intervals are unique.

<details>
<summary>Hint 1</summary>

How to check if an interval is covered by another?
</details>

<details>
<summary>Hint 2</summary>

Compare each interval to all others and check if it is covered by any interval.
</details>

<details>
<summary>Solution with Explanation</summary>

按照区间的起点进行升序排序：

.--------.
  .--------------.
     .-------.
       .---.
                    .---.
                      .------.

排序之后，两个相邻区间可能有如下三种情况：

1. 
```
.--------.
  .---.
```

2. 
```
.---------------.
        .---------------.
```

3. 
```
.-----.
         .------.
```


对于情况一，找到了覆盖区间。

对于情况二，两个区间可以合并，成一个大区间。

对于情况三，两个区间完全不相交。

依据几种情况，就可以写出代码了。

```java
class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        // 按照起点升序排列，起点相同时降序排列
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });

        // 记录合并区间的起点和终点
        int left = intervals[0][0];
        int right = intervals[0][1];

        int res = 0;
        for (int i = 1; i < intervals.length; i++) {
            int[] intv = intervals[i];
            // 情况一，找到覆盖区间
            if (left <= intv[0] && right >= intv[1]) {
                res++;
            }
            // 情况二，找到相交区间，合并
            if (right >= intv[0] && right <= intv[1]) {
                right = intv[1];
            }
            // 情况三，完全不相交，更新起点和终点
            if (right < intv[0]) {
                left = intv[0];
                right = intv[1];
            }
        }

        return intervals.length - res;
    }
}
```
</details>