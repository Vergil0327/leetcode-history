# Intuition

```
intervals = [[1,2],[2,3],[2,4],[4,5]]

1   2
    2     3
    2          4
               4     5
____
    ____
    ________
            ____
```

對於區間, 首先想到的是先排個序來看
由於要找minimum containing set => 代表每個區間裡的兩個數要盡可能重疊多個區間

所以我們先對end_time排序, 有點類似要找non-overlapping interval的感覺
盡可能將containing num放在end_time的話就能盡可能的重疊較多區間

從這想法去想的話, 第一個區間由前面沒有重疊, 我們就先放置1個在**end_time**跟另一個在**任意位置不管**
再來下個區間我們往前看跟一個區間重疊多少部分, 只要不是non-overlapping, 那至少會吃到前面的end_time num, 然後自己再放一個在end_time上
那這樣, 整個有overlapping intervals group就會是**size+1**個 containing nums

那這樣整個的minimum containing nums 就應該是sum(interval.size+1 for interval in overlapping_interval_group)

一開始想法是這樣, 但會在這test case上出錯:

```
intervals = [[1,3],[1,4],[2,5],[3,5]], expected=3, ex. [2,3,4]
1       3
1           4
    2           5
        3       5
_________
_____________
    _____________
        _________
```

會發現其實有些overlapping interval他不只涵蓋到前一個, 他還會涵蓋到前前一個overlapping interval
使得我們可以省更多的containing num

所以我們依照前面思想, 我們盡可能把兩個containing num放在`end_time`跟`end_time-1`, 讓他們盡可能跟後面的重疊的話
我們在遍歷過程中就要檢查:
- 如果當前overlapping_intervals[i].start_time <= 如果當前`overlapping_intervals[i-1].end_time-1`的話, 那麼當前的overlapping_intervals[i]就可以不用放任何的containing_num, 直接skip, 同時overlapping_interval_group的end_time也不變
- 如果當前overlapping_intervals[i]一樣跟前一個overlapping, 但overlapping_intervals[i].start_time沒有重疊到前一個的`end_time-1`的話, 那代表我們要再多放一個在overlapping_intervals[i].end_time, 同時紀錄前一個更近的containing num在overlapping_intervals[i-1].end_time

這樣看來我們對於每個overlapping_interval_group, 可能要持續記錄這兩個重疊的containing num的位置?

所以變成:

```py
intervals.sort(key=lambda x:x[1])

n = len(intervals)

overlapping_groups = [] # [containing_size, overlap1, overlap2] where overlap1 < overlap2
for i in range(n):
    if not overlapping_groups or overlapping_groups[-1][2] < intervals[i][0]:
        overlapping_groups.append([2, intervals[i][1]-1, intervals[i][1]])
    else:
        size, overlap1, overlap2 = overlapping_groups[-1]
        start, end = intervals[i]
        if start <= overlap1: continue
        overlapping_groups[-1] = [size+1, overlap2, end]

return sum(group[0] for group in overlapping_groups)
```

結果又fail在這個test case:
```
intervals=[[1,3],[3,7],[5,7],[7,8]], expected=5

1     3
      3           7
            5     7
                  7  8
```

這原因是因為:
截止至[3,7]為止, containing num = [2,3,7] => [size, overlap1, overlap2] = [3, 3, 7]
而[5,7]只重疊到overlap2的部分, 但由於他的end_time跟overlap2重合, 所以他不能放置在end_time位置, 只能更新overlap1成end_time-1位置
所以看來我們要更新overlap1, overlap2時得保證`overlap1<overlap2`並且當前的end_time是不是已經就是overlap2, 如果已經重疊, 已經是的話
我們只能更新overlap1成`interval[i].end_time-1`

所以概念上會是**greedily** update `overlap1` and `overlap2`, 盡可能讓overlap1跟overlap2往後重疊更多的區間