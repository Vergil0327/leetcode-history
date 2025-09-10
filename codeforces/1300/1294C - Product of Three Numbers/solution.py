# a * b * c = n where 2 <= a, b, c
# 找出所有prime factor, 然後湊出3個因數即可

t = int(input())
 
from math import isqrt
 
for _ in range(t):
    n = int(input())
    num = n
    prime_factor = []
    for i in range(2, isqrt(num)+1):
        if num%i == 0:
            while num%i == 0:
                prime_factor.append(i)
                num //= i
    if num > 1:
        prime_factor.append(num)
 
    ans = []
    while prime_factor:
        if len(ans) < 3 and prime_factor[-1] not in ans:
            ans.append(prime_factor.pop())
        elif len(ans) == 3:
            ans[-1] *= prime_factor.pop()
        else:
            x = prime_factor.pop()
            while prime_factor and x in ans:
                x *= prime_factor.pop()
            if x not in ans:
                ans.append(x)
            else:
                break
    if len(ans) == 3:
        print("YES")
        print(" ".join(map(str, ans)))
    else:
        print("NO")