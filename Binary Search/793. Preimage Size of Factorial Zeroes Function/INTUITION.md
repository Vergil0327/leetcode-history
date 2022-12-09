### Intuition

first, let's think how we can brute force it
based on the concept of *172. Factorial Trailing Zeroes*, we can calculate trailing zeros in logarithmic

and we just *linear search* to count

```python
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailingZeros(n):
            count = 0
            while n // 5 > 0:
                count += n // 5
                n //= 5
            return count
        cnt = 0

        for i in range(0, 2**32-1):
            if trailingZeros(i) > k: break
            if trailingZeros(i) == k:
                cnt += 1
        return cnt
```

the time complexity should be O(nlog5(n))

### Go Further

since trailing zeros is monotonically increasing, we can use **binary search** to replace linear search

once we use **binary search** to find upperbound and lowerbound

upperbound-lowerbound should be answer

time complexity is O(log2n * log5n)