# Intuition

first, we can get [brute force solution](https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/):

```py
n = len(s)
A, B = [], []
for i in range(n-len(a)+1):
    if s[i] == a[0] and s[i:i+len(a)] == a:
        A.append(i)
for i in range(n-len(b)+1):
    if s[i] == b[0] and s[i:i+len(b)] == b:
        B.append(i)
A.sort()
B.sort()

res = []
for i in A:
    r = bisect_right(B, i+k)
    l = bisect_left(B, i-k)
    if r-l > 0:
        res.append(i)
return res       
```

but now, we want to check if a (or b) in s in efficient way, not O(n^2)
=> maybe we can try rolling hash?

to check `a` in `s`:
we use a fixed-length sliding window, and check rolling_hash(s[i:i+len(a)]) == rolling_hash(a)
if True, append index to `A`

checking `b` in `s` is the same as above
if True, append index to `B`

then we can still find valid index by 

```py
A, B = rollingHash(s, a), rollingHash(s, b)
A.sort()
B.sort()

res = []
for i in A:
    r = bisect_right(B, i+k)
    l = bisect_left(B, i-k)
    if r-l > 0:
        res.append(i)
return res 
```