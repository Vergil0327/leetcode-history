# Intuition

first I think search space of speed: [1, max(dist)] -> WRONG!!!

>since we can have 2 decimal point, we can add 2 more digit.

>ex. dist[i] = 1e5 -> speed can be 1e7 and time equals 0.01

if current integer time we takes is 2.  hours = 2.1:
- if our speed is 1e7, we can reach successfully.
- if our speed search range only reach 1e5, time will be 1 and 2+1 > 2.1.

but 1e7 should be the answer rather than -1

ex. dist = [1,1,100000], hour = 2.01 -> answer = 10000000 not -1

the greater the speed is, the smaller the hour need and vice versa.
therefore,
we can binary search it and check if it's a possible answer

**Helper Function**

**check** function should use ceil to get integer hour.

but see example 2 and be careful of the final train we takes.
the final train don't need to take ceil of time

**do we always have answer ?**

not exactly, we can reach destination only if max speed is valid

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(1)$$