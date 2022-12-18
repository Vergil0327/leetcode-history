# Intuition

- find all the prime <= `n` first
- simulate manipulation

just one edge case to be careful:

```
ex. n = 4
4 = 2*2 and 2+2 = 4 -> it cause a dead loop
```

# Better Solution

inspired by this [post](https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/solutions/2923506/python-c-prime-factorization-explained/)

we don't need to find all the primes first

we can try from `2` to `n+1` and the process is just like what we do in finding primes

we always find all the `2` first, then `3`, then... `n prime`
we just keep finding until `n` equals to itself which means it's a prime already.