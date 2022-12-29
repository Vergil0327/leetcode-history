[1838. Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/)

`Medium`

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

```
Example 1:
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:
Input: nums = [3,9,6], k = 2
Output: 1
```

Constraints:

- 1 <= nums.length <= $10^5$
- 1 <= nums[i] <= $10^5$
- 1 <= k <= $10^5$

<details>
<summary>Hint</summary>

Note that you can try all values in a brute force manner and find the maximum frequency of that value.

</details>

<details>
<summary>Hint 2</summary>

To find the maximum frequency of a value consider the biggest elements smaller than or equal to this value

</details>

<details>
<summary>Solution</summary>

[original post](https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175181/java-python-prefix-sum-binary-search-o-nlogn/?orderBy=most_votes)


```py
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]

        def getSum(left, right):  # left, right inclusive
            return preSum[right + 1] - preSum[left]

        def count(index): # Count frequency of `nums[index]` if we make other elements equal to `nums[index]`
            left = 0
            right = index
            res = index
            while left <= right:
                mid = left + (right - left) // 2
                s = getSum(mid, index - 1) # get sum of (nums[mid], nums[mid+1]...nums[index-1])
                if s + k >= (index - mid) * nums[index]: # Found an answer -> Try to find a better answer in the left side
                    res = mid  # save best answer so far
                    right = mid - 1
                else:
                    left = mid + 1
            return index - res + 1

        ans = 0
        for i in range(n):
            ans = max(ans, count(i))
        return ans
```
</details>