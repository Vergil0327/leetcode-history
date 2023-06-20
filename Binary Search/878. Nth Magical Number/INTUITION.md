# Intuition

在a跟b的倍數中找出不重複的第n-th個, 要扣除最小公倍數

a 2a 3a 4a
b 2b 2b 4b
ab 2ab 3ab

see example 2:

a = 2, 4, 6
b = 3, 6, 9

最小公倍數lcm = a*b//gcd(a,b)

如果可以找到一個x使得恰好有n個matical number
x//a + x//b - x//lcm == n

那麼這個x就是magical number

=> binary search

```py
if x//a + x//b - x//lcm >= n:
    r = mid
else:
    l = mid+1
```