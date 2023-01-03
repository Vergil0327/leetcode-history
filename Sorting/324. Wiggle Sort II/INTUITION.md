# Time O(nlogn) Solution

## Intuition

based on definition of wiggle, if we sort in decreasing order,
we get first_sorted_half and second_sorted_half

the result after **Wiggle Sort** is zip(second_sorted_half, first_sorted_half)

## Complexity

- time complexity

$$O(nlogn)$$

- space complexity

$$O(n)$$

# Time O(n) Solution

## Intuition

use quickselect to find median and sort in decreasing order

after we quickselect median, we've also get two portion of nums

1. one portion with every num > median
2. the other portion with every num < median

based on definition of wiggle. or O(nlogn) solution above,

the result after **Wiggle Sort** is zip(second_sorted_half, first_sorted_half)

therefore, we can use side effect after **quickselect** and use extra O(n) space for:

- every nums[i] > median, put nums[i] in **odd** position in increasing direction

- every nums[i] < median, put in **even** position in reverse direction

- the empty position we stil have is where the `median` should put

and we update original nums

**Follow-Up O(1) solution is [here](https://leetcode.com/problems/wiggle-sort-ii/solutions/77682/step-by-step-explanation-of-index-mapping-in-java/)**