[1024. Video Stitching](https://leetcode.com/problems/video-stitching/description/)

`Medium`

You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths.

Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.

We can cut these clips into segments freely.

For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. If the task is impossible, return -1.

```
Example 1:
Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
Output: 3
Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].

Example 2:
Input: clips = [[0,1],[1,2]], time = 5
Output: -1
Explanation: We cannot cover [0,5] with only [0,1] and [1,2].

Example 3:
Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
Output: 3
Explanation: We can take clips [0,4], [4,7], and [6,9].
```

Constraints:

- 1 <= clips.length <= 100
- 0 <= starti <= endi <= 100
- 1 <= time <= 100

<details>
<summary>Hint 1</summary>

What if we sort the intervals? Considering the sorted intervals, how can we solve the problem with dynamic programming?

</details>

<details>
<summary>Hint 2</summary>

Let's consider a DP(pos, limit) where pos represents the position of the current interval we are gonna take the decision and limit is the current covered area from [0 - limit]. This DP returns the minimum number of taken intervals or infinite if it's not possible to cover the [0 - T] section.

</details>

<details>
<summary>Solution 1</summary>

[post](https://labuladong.github.io/algo/3/29/101/)
思路是先按照起点升序排序，如果起点相同的话按照终点降序排序，主要考虑到这道题的以下两个特点：

1、要用若干短视频凑出完成视频 [0, T]，至少得有一个短视频的起点是 0。

2、如果有几个短视频的起点都相同，那么一定应该选择那个最长（终点最大）的视频。

排序之后，从第一个区间开始选，每当选中一个区间 x（图中红色的区间），我们会比较所有起点小于 x.start 的区间，根据贪心策略，它们中终点最大的那个区间就是下一个会被选中的区间，以此类推。

```java
class Solution {
    public int videoStitching(int[][] clips, int T) {
        if (T == 0) return 0;
        // 按起点升序排列，起点相同的降序排列
        // PS：其实起点相同的不用降序排列也可以，不过我觉得这样更清晰
        Arrays.sort(clips, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });
        // 记录选择的短视频个数
        int res = 0;

        int curEnd = 0, nextEnd = 0;
        int i = 0, n = clips.length;
        while (i < n && clips[i][0] <= curEnd) {
            // 在第 res 个视频的区间内贪心选择下一个视频
            while (i < n && clips[i][0] <= curEnd) {
                nextEnd = Math.max(nextEnd, clips[i][1]);
                i++;
            }
            // 找到下一个视频，更新 curEnd
            res++;
            curEnd = nextEnd;
            if (curEnd >= T) {
                // 已经可以拼出区间 [0, T]
                return res;
            }
        }
        // 无法连续拼出区间 [0, T]
        return -1;
    }
}
```
</details>

<details>
<summary>Solution 2</summary>

[HuifengGuan](https://www.youtube.com/watch?v=ofzrZEQvHXY)
</details>

<details>
<summary>Solution 3</summary>

[Lee215](https://leetcode.com/problems/video-stitching/solutions/270036/java-c-python-greedy-solution-o-1-space/?orderBy=most_votes)

```python
def videoStitching(self, clips, T):
    end, end2, res = -1, 0, 0
    for i, j in sorted(clips):
        if end2 >= T or i > end2:
            break
        elif end < i <= end2:
            res, end = res + 1, end2
        end2 = max(end2, j)
    return res if end2 >= T else -1
```
</details>