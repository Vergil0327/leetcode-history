[2136. Earliest Possible Day of Full Bloom](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/)

`Hard`

You have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes time and so does the growth of a seed. You are given two 0-indexed integer arrays plantTime and growTime, of length n each:

plantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can work on planting exactly one seed. You do not have to work on planting the same seed on consecutive days, but the planting of a seed is not complete until you have worked plantTime[i] days on planting it in total.
growTime[i] is the number of full days it takes the ith seed to grow after being completely planted. After the last day of its growth, the flower blooms and stays bloomed forever.
From the beginning of day 0, you can plant the seeds in any order.

Return the earliest possible day where all seeds are blooming.

```
Example 1:
Input: plantTime = [1,4,3], growTime = [2,3,1]
Output: 9
Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 0, plant the 0th seed. The seed grows for 2 full days and blooms on day 3.
On days 1, 2, 3, and 4, plant the 1st seed. The seed grows for 3 full days and blooms on day 8.
On days 5, 6, and 7, plant the 2nd seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.

Example 2:
Input: plantTime = [1,2,3,2], growTime = [2,1,2,1]
Output: 9
Explanation: The grayed out pots represent planting days, colored pots represent growing days, and the flower represents the day it blooms.
One optimal way is:
On day 1, plant the 0th seed. The seed grows for 2 full days and blooms on day 4.
On days 0 and 3, plant the 1st seed. The seed grows for 1 full day and blooms on day 5.
On days 2, 4, and 5, plant the 2nd seed. The seed grows for 2 full days and blooms on day 8.
On days 6 and 7, plant the 3rd seed. The seed grows for 1 full day and blooms on day 9.
Thus, on day 9, all the seeds are blooming.

Example 3:
Input: plantTime = [1], growTime = [1]
Output: 2
Explanation: On day 0, plant the 0th seed. The seed grows for 1 full day and blooms on day 2.
Thus, on day 2, all the seeds are blooming.
```

Constraints:

n == plantTime.length == growTime.length
1 <= n <= 10^5
1 <= plantTime[i], growTime[i] <= 10^4

<details>
<summary>Hint 1</summary>

List the planting like the diagram above shows, where a row represents the timeline of a seed. A row i is above another row j if the last day planting seed i is ahead of the last day for seed j. Does it have any advantage to spend some days to plant seed j before completely planting seed i?
</details>

<details>
<summary>Hint 2</summary>

No. It does not help seed j but could potentially delay the completion of seed i, resulting in a worse final answer. Remaining focused is a part of the optimal solution.
</details>

<details>
<summary>Hint 3</summary>

Sort the seeds by their growTime in descending order. Can you prove why this strategy is the other part of the optimal solution? Note the bloom time of a seed is the sum of plantTime of all seeds preceding this seed plus the growTime of this seed.
</details>

<details>
<summary>Hint 4</summary>

There is no way to improve this strategy. The seed to bloom last dominates the final answer. Exchanging the planting of this seed with another seed with either a larger or smaller growTime will result in a potentially worse answer.
</details>

<details>
<summary>solution</summary>

[here](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/solution/)

 it is better to plant the seed with a longer growth time before the one with a shorter growth time. One may assume that it is always optimal to do so.

Let tt denote the answer to the problem, i.e. the minimum possible time when all flowers bloom. In an optimal solution, the seed ii has to begin growing no later than on the day t-growTime[i]t−growTime[i] so that it has enough time to grow until the day tt. The larger growTimegrowTime the seed has, the sooner it has to start to grow and the sooner we have to plant it.

One may already have an intuition to order the seeds by decreasing growth time. Let us prove it.

Consider an arbitrary optimal sequence of the seeds, i.e. the one that achieves the minimum possible time tt. Suppose there exist two adjacent seeds (there are no other seeds between them) ii and jj in this sequence such that the jj-th seed is planted after the ii-th one and growTime[i] \le growTime[j]growTime[i]≤growTime[j]. Let ss denote the day we begin planting the ii-th seed. We start to plant the jj-th seed on the day s+plantTime[i]s+plantTime[i] just after the ii-th seed. It takes plantTime[j]plantTime[j] to plant the jj-th seed and growTime[j]growTime[j] for it to grow. The jj-th seeds blooms on the day s+plantTime[i]+plantTime[j]+growTime[j]s+plantTime[i]+plantTime[j]+growTime[j]. The inequality s+plantTime[i]+plantTime[j]+growTime[j] \le ts+plantTime[i]+plantTime[j]+growTime[j]≤t must hold, because we consider the optimal sequence where all flowers, including the jj-th one, bloom not later than the day tt.

Let us see what happens when we swap these two seeds. Now we will plant the ii-th seed after the jj-th one. Such swap affects neither the previous seeds nor the next ones. It only changes the time when the ii-th and the jj-th flowers bloom. The seed jj blooms on the day s + plantTime[j] + growTime[j]s+plantTime[j]+growTime[j] and the ii-th one on the day s + plantTime[j] + plantTime[i] + growTime[i]s+plantTime[j]+plantTime[i]+growTime[i]. For the new sequence to remain optimal, the two flowers must still bloom before the day tt, i.e. the inequalities s + plantTime[j] + growTime[j] \le ts+plantTime[j]+growTime[j]≤t and s + plantTime[j] + plantTime[i] + growTime[i] \le ts+plantTime[j]+plantTime[i]+growTime[i]≤t must hold. The inequality from the previous paragraph implies these two inequalities, because plantTime[i] > 0plantTime[i]>0 and growTime[i] \le growTime[j]growTime[i]≤growTime[j].

Since we can achieve sorting by swapping, it is possible to sort any optimal sequence by decreasing of the growTimegrowTime with the described above swaps, without violating the optimality. It means the sorted sequence is optimal.

Algorithm
Sort the seeds by descending growth time. Plant the seeds in this order. For each, find the day it blooms and update the answer.
</details>