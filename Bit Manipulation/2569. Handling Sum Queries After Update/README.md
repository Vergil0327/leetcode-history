[2569. Handling Sum Queries After Update](https://leetcode.com/problems/handling-sum-queries-after-update/description/)

`Hard`

You are given two 0-indexed arrays nums1 and nums2 and a 2D array queries of queries. There are three types of queries:

For a query of type 1, queries[i] = [1, l, r]. Flip the values from 0 to 1 and from 1 to 0 in nums1 from index l to index r. Both l and r are 0-indexed.
For a query of type 2, queries[i] = [2, p, 0]. For every index 0 <= i < n, set nums2[i] = nums2[i] + nums1[i] * p.
For a query of type 3, queries[i] = [3, 0, 0]. Find the sum of the elements in nums2.
Return an array containing all the answers to the third type queries.

```
Example 1:
Input: nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
Output: [3]
Explanation: After the first query nums1 becomes [1,1,1]. After the second query, nums2 becomes [1,1,1], so the answer to the third query is 3. Thus, [3] is returned.

Example 2:
Input: nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
Output: [5]
Explanation: After the first query, nums2 remains [5], so the answer to the second query is 5. Thus, [5] is returned.
```

Constraints:

- 1 <= nums1.length,nums2.length <= 10^5
- nums1.length = nums2.length
- 1 <= queries.length <= 10^5
- queries[i].length = 3
- 0 <= l <= r <= nums1.length - 1
- 0 <= p <= 10^6
- 0 <= nums1[i] <= 1
- 0 <= nums2[i] <= 10^9

<details>
<summary>Hint</summary>

Use the Lazy Segment Tree to process the queries quickly.

</details>

```
1.   Maximum Length of Repeated Subarray
Medium
6K
150
Companies
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
```

```
712. Minimum ASCII Delete Sum for Two Strings
Medium
2.4K
69
Companies
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
```
