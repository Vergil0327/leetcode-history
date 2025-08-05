[3636. Threshold Majority Queries](https://leetcode.com/problems/threshold-majority-queries/)

`Hard`

You are given an integer array nums of length n and an array queries, where queries[i] = [li, ri, thresholdi].

Return an array of integers ans where ans[i] is equal to the element in the subarray nums[li...ri] that appears at least thresholdi times, selecting the element with the highest frequency (choosing the smallest in case of a tie), or -1 if no such element exists.

```
Example 1:
Input: nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]
Output: [1,-1,2]
Explanation:

Query	Sub-array	Threshold	Frequency table	Answer
[0, 5, 4]	[1, 1, 2, 2, 1, 1]	4	1 → 4, 2 → 2	1
[0, 3, 3]	[1, 1, 2, 2]	3	1 → 2, 2 → 2	-1
[2, 3, 2]	[2, 2]	2	2 → 2	2

Example 2:
Input: nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]
Output: [3,2,3,2]
Explanation:

Query	Sub-array	Threshold	Frequency table	Answer
[0, 6, 4]	[3, 2, 3, 2, 3, 2, 3]	4	3 → 4, 2 → 3	3
[1, 5, 2]	[2, 3, 2, 3, 2]	2	2 → 3, 3 → 2	2
[2, 4, 1]	[3, 2, 3]	1	3 → 2, 2 → 1	3
[3, 3, 1]	[2]	1	2 → 1	2
```

Constraints:

- 1 <= nums.length == n <= 10^4
- 1 <= nums[i] <= 10^9
- 1 <= queries.length <= 5 * 10^4
- queries[i] = [li, ri, thresholdi]
- 0 <= li <= ri < n
- 1 <= thresholdi <= ri - li + 1

Accepted
2,294/15.5K
Acceptance Rate
14.8%

<details>
<summary>Hint 1</summary>

Use sqrt decomposition: let B = int(sqrt(n)) and sort queries by (l//B, r)
</details>
<details>
<summary>Hint 2</summary>

Maintain window [L,R] with a frequency map cnt and buckets bucket[f] of values at count f
</details>
<details>
<summary>Hint 3</summary>

Slide L and R per query, updating cnt and bucket, then scan from threshold to max freq to find the smallest valid value or 1-
</details>