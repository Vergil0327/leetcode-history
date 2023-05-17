# Intuition

from observation, what we need is an smallest increasing subsequence lexicographically

thus, we can use a monotonically increasing stack to store our current optimal subsequence.

once we found a more promising value which means it's smaller than `stack[-1]`, we can greedily pop out stack.

```py
stack = []
for i, num in enumerate(nums):
    if not stack:
        stack.append(num)
    else:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
```

but be careful of constraint
because we need a subsequence whose length equals k, we must **NOT** pop out stack too much.

we need to make sure we have **at least** `k` length.

thus, we calculate remaining elements and only pop out stack while remaining elements are enough for us to build a k-length subsequence

```py
stack = []
for i, num in enumerate(nums):
    if not stack:
        stack.append(num)
    else:
        remain = n-1-i
        while stack and stack[-1] > num and len(stack)+remain >= k:
            stack.pop()
        stack.append(num)
```

# Complexity

- time complexity
$$O(n)$$

- sapce complexity
$$O(n)$$