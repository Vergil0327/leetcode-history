[1815. Maximum Number of Groups Getting Fresh Donuts](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/)

`Hard`

There is a donuts shop that bakes donuts in batches of batchSize. They have a rule where they must serve all of the donuts of a batch before serving any donuts of the next batch. You are given an integer batchSize and an integer array groups, where groups[i] denotes that there is a group of groups[i] customers that will visit the shop. Each customer will get exactly one donut.

When a group visits the shop, all customers of the group must be served before serving any of the following groups. A group will be happy if they all get fresh donuts. That is, the first customer of the group does not receive a donut that was left over from the previous group.

You can freely rearrange the ordering of the groups. Return the maximum possible number of happy groups after rearranging the groups.

```
Example 1:
Input: batchSize = 3, groups = [1,2,3,4,5,6]
Output: 4
Explanation: You can arrange the groups as [6,2,4,5,1,3]. Then the 1st, 2nd, 4th, and 6th groups will be happy.

Example 2:
Input: batchSize = 4, groups = [1,3,2,5,2,2,1,6]
Output: 4
``` 

Constraints:

- 1 <= batchSize <= 9
- 1 <= groups.length <= 30
- 1 <= groups[i] <= 10^9

<details>
<summary>Hint 1</summary>

The maximum number of happy groups is the maximum number of partitions you can split the groups into such that the sum of group sizes in each partition is 0 mod batchSize. At most one partition is allowed to have a different remainder (the first group will get fresh donuts anyway).

</details>
<details>
<summary>Hint 2</summary>

Suppose you have an array freq of length k where freq[i] = number of groups of size i mod batchSize. How can you utilize this in a dp solution?

</details>
<details>
<summary>Hint 3</summary>

Make a DP state dp[freq][r] that represents "the maximum number of partitions you can form given the current freq and current remainder r". You can hash the freq array to store it more easily in the dp table.

</details>
<details>
<summary>Hint 4</summary>

For each i from 0 to batchSize-1, the next DP state is dp[freq`][(r+i)%batchSize] where freq` is freq but with freq[i] decremented by 1. Take the largest of all of the next states and store it in ans. If r == 0, then return ans+1 (because you can form a new partition), otherwise return ans (continuing the current partition).

</details>