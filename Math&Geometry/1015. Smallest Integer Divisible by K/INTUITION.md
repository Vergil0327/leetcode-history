# Intuition

k*n = 1111111...

11...11 = 1111..10 + 1  (1 digit)
11...11 = 1111..100 + 11 (2 digits)
11...11 = 1111..1000 + 111 (3 digits)

ex. k=7
1 mod k = 1 => k * q1 + 1
11 mod k = 4 => k * q2 + 4
111 mod k = 6
1111 mod k = 5
...
111111 mod k = 0

if `11...11 mod k = 1` again, it means we already enter cycle,
because `11...11` can be written as `k * q' + 1`

once we find a cycle and we still have answer, return -1 directly
