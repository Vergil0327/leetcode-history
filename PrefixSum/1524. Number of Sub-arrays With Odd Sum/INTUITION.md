# Intuition

```
X X X X X X X X X X X
0                   i
```

- odd presum[0][i] - even presum[0][j] = odd presum[j][i]
    - odd presum[0][i] is also **one** valid odd sum
- even presum[0][i] - odd presum[0][j] = odd presum[j][i]

therefore, we should memorize number of all the prefix sum's parity, and:
1. if presum[i] is odd, res += 1 + number of even prefix sum
2. if presum[i] is even, res += number of odd prefix sum


# Complexity

time: O(n)
space: O(1)