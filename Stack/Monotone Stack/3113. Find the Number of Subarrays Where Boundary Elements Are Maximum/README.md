[3113. Find the Number of Subarrays Where Boundary Elements Are Maximum](https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/)

`Hard`

You are given an array of positive integers nums.

Return the number of subarrays of nums, where the first and the last elements of the subarray are equal to the largest element in the subarray.
 
```
Example 1:
Input: nums = [1,4,3,3,2]
Output: 6
Explanation:
There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray:

subarray [1,4,3,3,2], with its largest element 1. The first element is 1 and the last element is also 1.
subarray [1,4,3,3,2], with its largest element 4. The first element is 4 and the last element is also 4.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [1,4,3,3,2], with its largest element 2. The first element is 2 and the last element is also 2.
subarray [1,4,3,3,2], with its largest element 3. The first element is 3 and the last element is also 3.
Hence, we return 6.

Example 2:
Input: nums = [3,3,3]
Output: 6

Explanation:
There are 6 subarrays which have the first and the last elements equal to the largest element of the subarray:

subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
subarray [3,3,3], with its largest element 3. The first element is 3 and the last element is also 3.
Hence, we return 6.

Example 3:
Input: nums = [1]
Output: 1

Explanation:

There is a single subarray of nums which is [1], with its largest element 1. The first element is 1 and the last element is also 1.

Hence, we return 1.
```
 

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9

<details>
<summary>Hint 1</summary>

For each element nums[i], we can count the number of valid subarrays ending with it.

</details>
<details>
<summary>Hint 2</summary>

For each index i, find the nearest index j on its left (j < i) such that nums[j] < nums[i]. This can be done via a monotonic stack.

</details>
<details>
<summary>Hint 3</summary>

For each index i, find the number of indices k in the window [j + 1, i] such that nums[k] == nums[i], this is the number of the valid subarrays ending with nums[i]. This can be done by sliding window.

</details>
<details>
<summary>Hint 4</summary>

Sum the answer of all the indices i to get the final result.

</details>
<details>
<summary>Hint 5</summary>

Is it possible to use DSU as an alternate solution?

</details>