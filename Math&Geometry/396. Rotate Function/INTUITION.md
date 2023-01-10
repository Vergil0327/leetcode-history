# Intuition

let's see example 1: nums = [4,3,2,6]

we can observe that each time we rotate `nums`, the difference can be calculated in O(1) time complexity

define `k` is how many times we right-rotate

we can got recursive relation: T(n) = T(n-1) + SUM - arr_k[n-1] * n
and arr_k[n-1] is the last item in rotated nums.

thus, we can keep popping out last item to compute rotateSum from T(0) to T(n)

arr_0[n-1] = nums[n-1]
arr_1[n-1] = nums[n-2]
...

**right rotate**

4,3,2,6
6,4,3,2
2,6,4,3
3,2,6,4

rotateSum:
4*0 + 3*1 + 2*2 + 6*3
6*0 + 4*1 + 3*2 + 2*3
2*0 + 6*1 + 4*2 + 3*3
3*0 + 2*1 + 6*2 + 4*3

sum = sum(nums)
nextRotateSum = rotateSum + (sum-nums[n-1]) - nums[n-1] * (n-1)
              = rotateSum + sum - nums[n-1] * n

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(1)$$