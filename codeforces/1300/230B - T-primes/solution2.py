# nums[i] <= 10^12
# 但由於T-Prime必定是某個質數的平方, 所以我們isPrime的判斷, 只需要預先處理到10^6即可
# time:842 ms	memory:29300 KB

n = int(input())

from math import isqrt
def generatePrimeUntil(n: int):
    isPrime = [0, 0] + [1] * (n-2)

    for i in range(2, int(isqrt(n))+1):
        if not isPrime[i]: continue
        # all the factors before i*i have been considered at i-1, i-2, ..., 3, 2
        for j in range(i*i, n, i):
            isPrime[j] = 0
    return isPrime

isPrime = generatePrimeUntil(10**6+1)
nums = list(map(int, input().split()))


for num in nums:
    x = isqrt(num)
    if x*x == num and isPrime[x]:
        print("YES")
    else:
        print("NO")