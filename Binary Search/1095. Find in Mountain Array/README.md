[1095. Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)

`Hard`

(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

```
Example 1:
Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:
Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
```

Constraints:

- 3 <= mountain_arr.length() <= 10^4
- 0 <= target <= 10^9
- 0 <= mountain_arr.get(index) <= 10^9

<details>
<summary>Hint </summary>

Based on whether A[i-1] < A[i] < A[i+1], A[i-1] < A[i] > A[i+1], or A[i-1] > A[i] > A[i+1], we are either at the left side, peak, or right side of the mountain. We can binary search to find the peak. After finding the peak, we can binary search two more times to find whether the value occurs on either side of the peak.
</details>

<details>
<summary>Solution</summary>

[Discussion](https://leetcode.com/problems/find-in-mountain-array/discuss/317607/JavaC%2B%2BPython-Triple-Binary-Search)

1. Binary find peak in the mountain.
   [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/139848/C%2B%2BJavaPython-Better-than-Binary-Search/294082)

2. Binary find the target in strict increasing array
3. Binary find the target in strict decreasing array

```
Tip
Personally,
If I want find the index, I always use while (left < right)
If I may return the index during the search, I'll use while (left <= right)
```

```python
def findInMountainArray(self, target, A):
        n = A.length()
        # find index of peak
        l, r = 0, n - 1
        while l < r:
            m = (l + r) / 2
            if A.get(m) < A.get(m + 1):
                l = peak = m + 1
            else:
                r = m
        # find target in the left of peak
        l, r = 0, peak
        while l <= r:
            m = (l + r) / 2
            if A.get(m) < target:
                l = m + 1
            elif A.get(m) > target:
                r = m - 1
            else:
                return m
        # find target in the right of peak
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) / 2
            if A.get(m) > target:
                l = m + 1
            elif A.get(m) < target:
                r = m - 1
            else:
                return m
        return -1
```
</details>

