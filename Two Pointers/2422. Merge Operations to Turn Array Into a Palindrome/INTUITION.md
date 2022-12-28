# Two Pointers

## Intuition

since the final answer is a `Palindrome`, which means the left-most num equals to right-most num, we can use two pointers to track `leftSum` and `rightSum`.

the smaller one in `leftSum` and `rightSum` should be added some nums[i] to make both equal, thus, we always move pointer of smaller sum.

once `leftSum` equals to `rightSum`, update two pointers and re-init `leftSum` and `rightSum`. keep doing operation until two pointers meet each other.

since every single num is a `Palindrome`, there must exist a solution.

## Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(1)$$