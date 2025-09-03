#### TLE
# n = int(input())

# from math import isqrt
# def check(num):
#     cnt = 0 # [1,num, ... ?]
#     for i in range(1, isqrt(num)+1):
#         if num%i == 0:
#             cnt += 1
#             if num//i != i:
#                 cnt += 1
#         if cnt > 3: return False
#     return cnt == 3

# nums = list(map(int, input().split()))
# for num in nums:
#     if check(num):
#         print("YES")
#     else:
#         print("NO")

# 仔細想想, 所謂的T-Prime不就是有整數平方根質數的數嗎?

# 2^2 = 4  => YES, 質數
# 3^2 = 9  => YES, 質數
# 4^2 = 16 => NO, 4非質數
# 5^2 = 25 => YES, 5是質數
# 那這樣一來一切就簡單了, 只需要找出平方根為整數且同時為質數的數即為"YES"


n = int(input())

def isPrime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

nums = list(map(int, input().split()))

from math import isqrt
for num in nums:
    x = isqrt(num)
    if x*x == num and isPrime(x):
        print("YES")
    else:
        print("NO")