"""
簡單講:
單程票: 票價a
m程票: 票價b

要搭乘n趟, 該怎麼買比較好
"""

### method 1 - brute force
# try every possible ways
from math import ceil
 
n, m, a, b = list(map(int, input().split()))
 
 
x = ceil(n/m)
 
res = float('inf')
for i in range(x+1):
    res = min(res, b * i + max(0, (n-i*m)) * a)
print(res)

### method 2 - math
# since m rides cost b, if m * a <= b, we don't need m-ride tickets
# then, break into 2 possible solution
# 1. only buy m-ride ticket to cover `n` riders
# 2. but `n//m` m-ride ticket and `n%m` one-way ticket
# choose cheaper one
 
n, m, a, b = list(map(int, input().split()))
if m * a <= b:
    print(n*a)
else:
    x = n//m
    print(min(x * b + (n%m) * a, (x+1) * b))