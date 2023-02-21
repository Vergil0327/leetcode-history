# Intuition

the description said we must solve in $O(logn)$ time, we can directly come up with **Binary Search**

then I start thinking should I **search by value** or **search by index** ?

>example.
    ```
    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2
    ```

- If I search by value:
search space: [1, 8]
mid = 4
then I have no information to decide I should ignore left-half or right half

- what if I search by index ?:
n = len(nums) = 9
search sapce: [0, n-1] = [0, 8]
mid = 4
nums[mid] = 3

then we can use $$O(1)$$ to check left and right
if none of left and right equals nums[mid], then we found the answer!

if not, the only information we have is index, `l`, `r` and `n`
then I observe `nums` and realize since nums[i] should be pair except answer, the left-half or right-half should be either **even number** or **odd number**

then, we can easily choose what half we should continue to binary search.

- if number of left-half is even, answer must exist in right-half
    - if nums[mid] = nums[mid+1]
        - left-half = [l, mid-1]
        - right-half = [mid+2, r]
    - if nums[mid] = nums[mid-1]
        - left-half = [l, mid-2]
        - right-half = [mid+1, r]
- if number of right-half is even, answer must exist in left-half

then we can implement binary search easily.

# Complexity
- Time complexity:
$$O(logn)$$

- Space complexity:
$$O(1)$$
