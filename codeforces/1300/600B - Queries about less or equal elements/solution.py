n, m = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

from bisect import bisect_right

res = []
for num in b:
    res.append(str(bisect_right(a, num)))

print(" ".join(res))