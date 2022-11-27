similar solution:
- [Balance](https://leetcode.com/problems/count-subarrays-with-median-k/discuss/2851940/Balance)
- [freq-table](https://leetcode.com/problems/count-subarrays-with-median-k/discuss/2852127/Python3-freq-table)

the concepts is just like **Two Sum**

1. we found the index of median first
   -  valid subarray must contain median

2. and we know that:
   - if array is odd, # of number greater than median - # of number smaller than median will equal to `0`, we got 1 valid answer
   - if array is even, # of number greater than median - # of number smaller than median will equal to `1`, we got 1 valid answer

so, we count # of (greater-than-median - smaller-than-median) from median backward at each position first

then, we start from median's position to the end forward and find if there exist a complement subarray. add its count to answer

ex.      [1, 2, 3, 4, 5], k = 3
balance  -2 -1  0
counter = {0: 1, -1: 1, -2: 1}

then we start from **3** to **5** to calculate

ex.      [1, 2, 3, 4, 5], k = 3
balance         0  1  2
iterate at 3: ans += counter[-0] + counter[1-0]
iterate at 4: ans += counter[-1] (we need subarray which can make current subarray balacne to 0) + counter[1-1] (we need subarray which can make current balance to 1)
iterate at 5: ans += counter[-2] + counter[1-2]
