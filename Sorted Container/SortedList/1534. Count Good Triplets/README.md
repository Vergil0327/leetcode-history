[1534. Count Good Triplets](https://leetcode.com/problems/count-good-triplets)

`Easy`

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

- 0 <= i < j < k < arr.length
- |arr[i] - arr[j]| <= a
- |arr[j] - arr[k]| <= b
- |arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

```
Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

Example 2:
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
``` 

Constraints:

- 3 <= arr.length <= 100
- 0 <= arr[i] <= 1000
- 0 <= a, b, c <= 1000

Accepted
142.8K
Submissions
173.9K
Acceptance Rate
82.1%

<details>
<summary>Hint 1</summary>

Notice that the constraints are small enough for a brute force solution to pass.

</details>
<details>
<summary>Hint 2</summary>

Loop through all triplets, and count the ones that are good.

</details>
