[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

`Medium`

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

```
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

Constraints:

- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

<details>
<summary>Solution</summary>

區間可以表示為 [start, end]
按 start 排序後對於相交區間合併後結果，最初的 new_interval.start一定是相交裡最小的，而 new_interval.end一定是裡面最大

由於已經排序，因此就已經確定new_interval.start，那麼new_interval.end就只要找最大值即可

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        LinkedList<int[]> res = new LinkedList<>();
        // sort start in increasing order
        Arrays.sort(intervals, (a, b) -> {
            return a[0] - b[0];
        });

        res.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            int[] curr = intervals[i];
            
            // last interval in `res`
            int[] last = res.getLast();
            if (curr[0] <= last[1]) {
                last[1] = Math.max(last[1], curr[1]);
            } else {
                // next interval wait to process
                res.add(curr);
            }
        }
        return res.toArray(new int[0][0]);
    }
}
```
</details>